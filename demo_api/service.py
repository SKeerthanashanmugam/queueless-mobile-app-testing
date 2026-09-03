import sqlite3
from contextlib import contextmanager
from pathlib import Path


SCHEMA = """
CREATE TABLE IF NOT EXISTS slots(id TEXT PRIMARY KEY, doctor_id TEXT NOT NULL, status TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS appointments(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id TEXT NOT NULL, slot_id TEXT NOT NULL, status TEXT NOT NULL);
CREATE UNIQUE INDEX IF NOT EXISTS one_active_booking_per_slot ON appointments(slot_id) WHERE status='CONFIRMED';
CREATE TABLE IF NOT EXISTS payments(id INTEGER PRIMARY KEY AUTOINCREMENT, appointment_id INTEGER NOT NULL, idempotency_key TEXT UNIQUE NOT NULL, amount REAL NOT NULL, status TEXT NOT NULL);
"""


class QueueLessService:
    def __init__(self, database=":memory:"):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(SCHEMA)
        self.connection.execute("INSERT OR IGNORE INTO slots VALUES ('S001','D001','AVAILABLE')")
        self.connection.execute("INSERT OR IGNORE INTO slots VALUES ('S002','D001','AVAILABLE')")
        self.connection.commit()

    def health(self):
        return {"status": "ok"}

    def search_doctors(self, specialty):
        doctors = [{"id": "D001", "name": "Dr Meena Raman", "specialty": "Cardiology"}]
        return [d for d in doctors if specialty.lower() in d["specialty"].lower()]

    def book(self, patient_id, slot_id):
        slot = self.connection.execute("SELECT * FROM slots WHERE id=?", (slot_id,)).fetchone()
        if not slot or slot["status"] != "AVAILABLE":
            raise ValueError("Slot is unavailable")
        try:
            cursor = self.connection.execute(
                "INSERT INTO appointments(patient_id,slot_id,status) VALUES (?,?, 'CONFIRMED')",
                (patient_id, slot_id),
            )
            self.connection.execute("UPDATE slots SET status='BOOKED' WHERE id=?", (slot_id,))
            self.connection.commit()
        except sqlite3.IntegrityError as exc:
            self.connection.rollback()
            raise ValueError("Slot is unavailable") from exc
        return {"appointment_id": cursor.lastrowid, "status": "CONFIRMED"}

    def pay(self, appointment_id, idempotency_key, amount):
        existing = self.connection.execute(
            "SELECT * FROM payments WHERE idempotency_key=?", (idempotency_key,)
        ).fetchone()
        if existing:
            return dict(existing)
        appointment = self.connection.execute(
            "SELECT * FROM appointments WHERE id=?", (appointment_id,)
        ).fetchone()
        if not appointment or appointment["status"] != "CONFIRMED" or amount <= 0:
            raise ValueError("Invalid payment request")
        cursor = self.connection.execute(
            "INSERT INTO payments(appointment_id,idempotency_key,amount,status) VALUES (?,?,?,'SUCCESS')",
            (appointment_id, idempotency_key, amount),
        )
        self.connection.commit()
        return dict(self.connection.execute("SELECT * FROM payments WHERE id=?", (cursor.lastrowid,)).fetchone())

    def cancel(self, appointment_id):
        appointment = self.connection.execute("SELECT * FROM appointments WHERE id=?", (appointment_id,)).fetchone()
        if not appointment or appointment["status"] != "CONFIRMED":
            raise ValueError("Appointment cannot be cancelled")
        self.connection.execute("UPDATE appointments SET status='CANCELLED' WHERE id=?", (appointment_id,))
        self.connection.execute("UPDATE slots SET status='AVAILABLE' WHERE id=?", (appointment["slot_id"],))
        self.connection.commit()
        return {"appointment_id": appointment_id, "status": "CANCELLED"}

