# Executable QueueLess Reference Service

This dependency-free Python/SQLite service models the core booking and payment rules so the repository includes genuinely executable tests. It is not presented as the Android/iOS application.

Run from the repository root:

```bash
python -m unittest discover -s demo_api/tests -v
```

Coverage includes health, search, successful booking, unavailable slots, double-booking prevention, payment validation, payment idempotency and cancellation slot release.

