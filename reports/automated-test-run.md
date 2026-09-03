# Automated Test Execution Report

## Execution record

| Field | Value |
|---|---|
| Execution date | 2026-09-03 UTC |
| Component | QueueLess Python/SQLite reference service |
| Command | `python -m unittest discover -s demo_api/tests -v` |
| Runtime | Python 3.12.3, Linux |
| Total | 10 |
| Passed | 10 |
| Failed | 0 |
| Errors | 0 |
| Result | PASS |

## Executed checks

| Automated test | Result |
|---|---|
| Health response | Pass |
| Search matching specialty | Pass |
| Search unknown specialty | Pass |
| Book available slot | Pass |
| Prevent double booking | Pass |
| Reject unknown slot | Pass |
| Successful payment | Pass |
| Payment idempotency | Pass |
| Reject invalid payment | Pass |
| Cancellation releases slot | Pass |

## Console output

```text
test_01_health ... ok
test_02_search_matching_specialty ... ok
test_03_search_unknown_specialty ... ok
test_04_book_available_slot ... ok
test_05_prevent_double_booking ... ok
test_06_reject_unknown_slot ... ok
test_07_payment_success ... ok
test_08_payment_is_idempotent ... ok
test_09_reject_invalid_payment ... ok
test_10_cancel_releases_slot ... ok

Ran 10 tests in 0.003s
OK
```

## Scope statement

This is genuine execution evidence for the included reference service. It does not claim execution of the separate 70 manual Android/iOS test cases or the Appium starter tests, which require an authorized APK and configured device/emulator.

