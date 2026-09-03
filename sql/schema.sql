-- Minimal reference schema for local QA practice; not a production design.
CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, mobile VARCHAR(15) UNIQUE NOT NULL);
CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, specialty VARCHAR(80), active BOOLEAN NOT NULL);
CREATE TABLE slots (slot_id INTEGER PRIMARY KEY, doctor_id INTEGER NOT NULL, starts_at TIMESTAMP NOT NULL, status VARCHAR(20) NOT NULL, UNIQUE(doctor_id, starts_at));
CREATE TABLE appointments (appointment_id INTEGER PRIMARY KEY, patient_id INTEGER NOT NULL, slot_id INTEGER NOT NULL, status VARCHAR(20) NOT NULL, created_at TIMESTAMP NOT NULL);
CREATE TABLE payments (payment_id INTEGER PRIMARY KEY, appointment_id INTEGER NOT NULL, idempotency_key VARCHAR(80) UNIQUE NOT NULL, amount DECIMAL(10,2) NOT NULL, status VARCHAR(20) NOT NULL);
CREATE TABLE refunds (refund_id INTEGER PRIMARY KEY, payment_id INTEGER NOT NULL, amount DECIMAL(10,2) NOT NULL, status VARCHAR(20) NOT NULL);

