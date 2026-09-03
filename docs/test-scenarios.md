# Test Scenarios

| ID | Module | Scenario | Type | Priority |
|---|---|---|---|---:|
| TS-001 | Install | Fresh install, update, permissions and uninstall | Compatibility | P1 |
| TS-002 | Login | Valid, invalid, expired and reused OTP | Functional/Security | P0 |
| TS-003 | Login | Resend countdown and request rate limiting | Boundary | P1 |
| TS-004 | Session | Logout, token expiry and background timeout | Security | P0 |
| TS-005 | Search | Search by doctor, specialty and hospital | Functional | P0 |
| TS-006 | Filters | Combine, remove and reset filters | Functional/UI | P1 |
| TS-007 | Profile | Validate doctor details, fee and location | Data/UI | P1 |
| TS-008 | Slots | Validate available, expired and concurrent slot states | Functional | P0 |
| TS-009 | Booking | Create booking and prevent duplicate booking | Functional/Data | P0 |
| TS-010 | Payment | Success, decline, timeout, retry and duplicate callback | Functional/API | P0 |
| TS-011 | Interruption | Call/SMS/background during payment | Recovery | P0 |
| TS-012 | Reschedule | Move booking and atomically release old slot | Functional/Data | P1 |
| TS-013 | Cancellation | Policy boundary and refund calculation | Functional | P1 |
| TS-014 | Notification | Correct reminder, deep link and privacy | Functional/Security | P1 |
| TS-015 | Prescription | Authorized view/download; block other patient | Security | P0 |
| TS-016 | Network | Offline, slow, switching Wi-Fi/mobile data | Resilience | P0 |
| TS-017 | Compatibility | OS, screen size, orientation and theme | Compatibility | P1 |
| TS-018 | Accessibility | TalkBack/VoiceOver, font scaling, contrast and targets | Accessibility | P1 |
| TS-019 | Localization | English/Tamil, dates, time and clipping | Localization | P2 |
| TS-020 | Performance | Launch and primary-screen response observations | Performance | P1 |
| TS-021 | Emergency | Available/unavailable emergency request and fallback | Functional | P0 |
| TS-022 | Data | Appointment/payment/refund database consistency | Database | P0 |

