# Mobile Test Plan

## Objective

Assess whether QueueLess provides a reliable, usable and secure appointment journey across supported Android and iOS devices, with special attention to booking and payment consistency.

## In scope

- Installation/update/uninstallation
- Registration, OTP and session handling
- Search, filters, profiles and slots
- Booking, payment, reschedule, cancellation and refund
- Notifications, prescription access and profile
- Functional, UI, usability, exploratory, compatibility, interruption, network, accessibility and localization checks
- API and database validation where authorized access exists
- Smoke automation for stable critical flows

## Out of scope

- Production penetration testing
- Real financial transactions
- Clinical accuracy of medical advice
- Production load testing without written authorization
- Third-party provider internals

## Test approach

| Level | Approach |
|---|---|
| P0 smoke | Launch, login, search, book, payment callback, appointment display |
| P1 regression | Positive/negative boundaries across all core modules |
| Risk-based | Concurrency, retry/idempotency, session privacy, interruption and recovery |
| Exploratory | 60-minute charters for booking, payment and accessibility |
| Automation | Stable smoke and regression candidates; manual coverage retained for usability/interruption |

## Entry criteria

- Approved requirements and acceptance criteria
- Installable test build with release notes
- Stable staging environment, test data and credentials
- Supported-device list and known-issues list

## Exit criteria

- 100% P0 and at least 95% planned P1 cases executed
- No open Blocker/Critical defects; High defects accepted with documented business decision
- Core API and database integrity checks pass
- Test summary reviewed with unresolved risks listed

## Suspension/resumption

Suspend if build cannot launch, staging is unavailable for over 30 minutes, OTP/payment sandbox is unusable, or data corruption prevents meaningful execution. Resume after a verified fix/build and smoke test.

## Defect severity

| Severity | Meaning | Example |
|---|---|---|
| S1 Blocker | Testing/core service impossible | App crash on launch |
| S2 Critical | Major business/data/security failure | Double charge or unauthorized prescription access |
| S3 Major | Important feature fails with workaround | Filter produces incorrect results |
| S4 Minor | Limited functional/UI impact | Alignment issue on one screen |
| S5 Trivial | Cosmetic improvement | Minor spacing inconsistency |

## Deliverables

Requirements, test plan, scenarios, detailed cases, RTM, device/network matrix, test data, API collection, SQL checks, automation suite, defect records, evidence, execution report and summary report.

## Risks and mitigation

| Risk | Mitigation |
|---|---|
| No iOS hardware | Use simulator initially; explicitly mark hardware-only coverage pending |
| Dynamic OTP/payment dependency | Use approved sandbox/stubs and test retry/callback states |
| Device fragmentation | Select risk-based representative physical and virtual devices |
| Personal health data exposure | Use synthetic data only and redact evidence |

