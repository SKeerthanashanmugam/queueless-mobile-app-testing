-- Run only against an authorized QA database. Adapt syntax/table names to the actual schema.

-- 1. More than one active appointment for the same slot (must return zero rows).
SELECT slot_id, COUNT(*) AS active_count
FROM appointments
WHERE status IN ('CONFIRMED','IN_PROGRESS')
GROUP BY slot_id
HAVING COUNT(*) > 1;

-- 2. Successful payment without a confirmed/completed appointment (zero rows).
SELECT p.payment_id, p.appointment_id, a.status
FROM payments p LEFT JOIN appointments a ON a.appointment_id = p.appointment_id
WHERE p.status = 'SUCCESS' AND (a.appointment_id IS NULL OR a.status NOT IN ('CONFIRMED','COMPLETED','CANCELLED'));

-- 3. Duplicate idempotency keys (zero rows; also protected by unique constraint).
SELECT idempotency_key, COUNT(*)
FROM payments GROUP BY idempotency_key HAVING COUNT(*) > 1;

-- 4. Refund exceeding original successful payment (zero rows).
SELECT r.refund_id, r.amount AS refund_amount, p.amount AS paid_amount
FROM refunds r JOIN payments p ON p.payment_id = r.payment_id
WHERE r.amount > p.amount;

-- 5. Slots marked available while linked to active booking (zero rows).
SELECT s.slot_id, s.status, a.appointment_id
FROM slots s JOIN appointments a ON a.slot_id = s.slot_id
WHERE s.status = 'AVAILABLE' AND a.status IN ('CONFIRMED','IN_PROGRESS');

-- 6. Orphan appointments (zero rows).
SELECT a.appointment_id
FROM appointments a
LEFT JOIN patients p ON p.patient_id = a.patient_id
LEFT JOIN slots s ON s.slot_id = a.slot_id
WHERE p.patient_id IS NULL OR s.slot_id IS NULL;

-- 7. Daily booking/payment reconciliation.
SELECT DATE(a.created_at) AS booking_date,
       COUNT(DISTINCT a.appointment_id) AS appointments,
       SUM(CASE WHEN p.status='SUCCESS' THEN 1 ELSE 0 END) AS successful_payments,
       COALESCE(SUM(CASE WHEN p.status='SUCCESS' THEN p.amount ELSE 0 END),0) AS collected_amount
FROM appointments a LEFT JOIN payments p ON p.appointment_id=a.appointment_id
GROUP BY DATE(a.created_at) ORDER BY booking_date DESC;

