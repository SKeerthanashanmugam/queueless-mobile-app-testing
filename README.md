# QueueLess – Smart Hospital Appointment Mobile App Testing

Portfolio QA project demonstrating manual mobile testing for an Android/iOS hospital appointment application, supported by API, database, accessibility, compatibility, and Appium automation assets.

**Portfolio status:** A working QueueLess Android application is included in `android-app/`. The app was built and installed on a physical OPPO CPH2495 running Android 15. Nine manual smoke/critical-path tests, Android unit and instrumented tests, and ten Python/SQLite automated tests have been genuinely executed. The remaining manual cases are clearly marked Not Run.

## Product under test

QueueLess enables patients to register, find doctors, book/reschedule/cancel appointments, pay fees, receive reminders, and view prescriptions. The highest-risk flows are authentication, booking concurrency, payment integrity, privacy, and emergency access.

## What this repository demonstrates

- Requirement analysis and risk-based test planning
- Android/iOS functional, UI, usability, compatibility, interruption, network, accessibility, localization, and security-oriented testing
- Traceable test scenarios and detailed test cases
- Jira-style defect documentation templates and realistic example defects clearly marked as samples
- REST API checks using Postman/Newman
- SQL validation queries for appointment and payment integrity
- Appium + Pytest automation starter framework
- Test execution, daily status, and summary reporting templates

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Requirements, test plan, strategy, RTM, matrices, reports and interview guide |
| `test-cases/` | Detailed manual cases and test data |
| `defects/` | Defect template and sample defect reports |
| `api/` | Postman collection and environment |
| `sql/` | Schema and data-integrity validation queries |
| `automation/` | Appium/Pytest framework with page objects |
| `demo_api/` | Executable Python/SQLite reference service and automated integration tests |
| `reports/` | Committed evidence from genuine automated test runs |
| `evidence/` | Screenshot placeholder and evidence naming guide |
| `android-app/` | Working Kotlin/Jetpack Compose Android application tested on a physical device |

## Suggested application scope

1. OTP registration/login
2. Doctor search and filters
3. Slot selection and appointment booking
4. Reschedule/cancellation
5. Payment, failure recovery and refund
6. Push reminders
7. Prescription/report access
8. Profile and logout

## Quick start: automation

Prerequisites: Python 3.10+, Node.js, Appium 2, Android SDK, a running emulator/device, and the QueueLess APK.

```bash
cd automation
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
appium driver install uiautomator2
appium
pytest -v --html=reports/report.html --self-contained-html
```

Set `QUEUELESS_APP` to the absolute APK path or edit `automation/config.json`. Replace the example accessibility IDs in page objects with identifiers from the actual app build.

## Run the verified reference-service tests

No external packages are required:

```bash
python -m unittest discover -s demo_api/tests -v
```

## Quick start: API

Import the collection and environment from `api/` into Postman. Replace `base_url` with the available test API and run in the Collection Runner. CLI option:

```bash
newman run api/QueueLess.postman_collection.json -e api/QueueLess.local.postman_environment.json
```

## Execution workflow

1. Obtain an authorized test build and requirements.
2. Update build/device details in `docs/test-execution-report.md`.
3. Execute cases in `test-cases/manual-test-cases.csv`.
4. Save evidence using `evidence/README.md` naming rules.
5. Log observed defects using `defects/defect-template.md`.
6. Run API, SQL and automation checks where access is available.
7. Complete `docs/test-summary-report.md` with actual totals.


## API testing execution

REST API testing was completed using Postman against the local Python reference API.

- 7 API requests executed
- 11 test assertions passed
- 0 failures and 0 errors
- Average response time: 8 ms
- Covered health, OTP, doctor search, slots, appointment creation/retrieval, and unauthorized-access validation

Run the local API:

```powershell
python demo_api/server.py
```
Evidence: `evidence/screenshots/API-Postman-Collection-Run.png`

Detailed results: `docs/api-test-execution-report.md`

## Database and service testing execution

Executed Python `unittest` validations against the SQLite-backed service.

- 10 tests executed
- 10 tests passed
- 100% pass rate
- 0 failures and 0 errors
- Validated booking, double-booking prevention, payments, cancellation and data consistency

Evidence: `evidence/screenshots/DB-Test-Results.png`

Detailed results: `docs/database-test-execution-report.md`

## Author

Keerthana S — Software Testing portfolio project
