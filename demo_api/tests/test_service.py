import unittest

from demo_api.service import QueueLessService


class QueueLessServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = QueueLessService()

    def test_01_health(self):
        self.assertEqual(self.service.health(), {"status": "ok"})

    def test_02_search_matching_specialty(self):
        self.assertEqual(len(self.service.search_doctors("cardiology")), 1)

    def test_03_search_unknown_specialty(self):
        self.assertEqual(self.service.search_doctors("neurology"), [])

    def test_04_book_available_slot(self):
        self.assertEqual(self.service.book("P001", "S001")["status"], "CONFIRMED")

    def test_05_prevent_double_booking(self):
        self.service.book("P001", "S001")
        with self.assertRaisesRegex(ValueError, "unavailable"):
            self.service.book("P002", "S001")

    def test_06_reject_unknown_slot(self):
        with self.assertRaisesRegex(ValueError, "unavailable"):
            self.service.book("P001", "UNKNOWN")

    def test_07_payment_success(self):
        appointment = self.service.book("P001", "S001")
        payment = self.service.pay(appointment["appointment_id"], "KEY-001", 500)
        self.assertEqual(payment["status"], "SUCCESS")

    def test_08_payment_is_idempotent(self):
        appointment = self.service.book("P001", "S001")
        first = self.service.pay(appointment["appointment_id"], "KEY-001", 500)
        second = self.service.pay(appointment["appointment_id"], "KEY-001", 500)
        self.assertEqual(first["id"], second["id"])
        count = self.service.connection.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
        self.assertEqual(count, 1)

    def test_09_reject_invalid_payment(self):
        with self.assertRaisesRegex(ValueError, "Invalid"):
            self.service.pay(999, "KEY-X", 500)

    def test_10_cancel_releases_slot(self):
        appointment = self.service.book("P001", "S001")
        self.service.cancel(appointment["appointment_id"])
        replacement = self.service.book("P002", "S001")
        self.assertEqual(replacement["status"], "CONFIRMED")


if __name__ == "__main__":
    unittest.main(verbosity=2)

