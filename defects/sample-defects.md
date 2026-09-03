# Sample Defect Reports

> Illustrative examples for demonstrating defect-writing skill. These are not defects observed in a real QueueLess build.

## SAMPLE-BUG-001 — Repeated Pay tap creates two payment requests

| Field | Value |
|---|---|
| Module | Payment |
| Severity / priority | S2 Critical / P0 |
| Environment | Hypothetical Android staging build |
| Related case | TC-034 |

**Preconditions:** An unpaid appointment exists and network latency is high.  
**Steps:** Open payment → select card → rapidly tap Pay twice → inspect requests/appointment.  
**Expected:** Pay becomes disabled after first tap; one idempotent request and one charge exist.  
**Illustrative actual:** Two requests with different identifiers are submitted and both show processing.  
**Risk:** Possible double charge and reconciliation failure.

## SAMPLE-BUG-002 — Tamil doctor name is clipped at 200% font size

| Field | Value |
|---|---|
| Module | Doctor profile |
| Severity / priority | S4 Minor / P2 |
| Environment | Hypothetical small-screen Android device |
| Related case | TC-066, TC-069 |

**Steps:** Select Tamil → set system font to 200% → open a doctor profile with a long name.  
**Expected:** Full name remains readable or wraps without overlapping actions.  
**Illustrative actual:** Second line overlaps the Book button.

