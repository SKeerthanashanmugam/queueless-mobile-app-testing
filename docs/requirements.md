# Software Requirements Specification

## Personas

- Patient: searches, books, pays and manages appointments.
- Doctor: views schedule and updates consultation status.
- Hospital administrator: manages doctors, slots and refunds.

## Functional requirements

| ID | Requirement | Priority | Acceptance criteria |
|---|---|---:|---|
| FR-01 | Register/login using mobile number and OTP | Critical | Valid OTP opens home; invalid/expired OTP is rejected; resend is rate-limited |
| FR-02 | Search doctors by name, specialty and hospital | High | Relevant active doctors are returned with available dates |
| FR-03 | Filter by specialty, date, language, gender and fee | Medium | Results reflect all selected filters and can be reset |
| FR-04 | View doctor profile and live slots | High | Profile, fee, location and available slots are accurate |
| FR-05 | Book one available slot | Critical | Confirmed booking has unique ID; same slot cannot be double-booked |
| FR-06 | Pay consultation fee | Critical | Exactly one payment is linked to one booking; retry is idempotent |
| FR-07 | Reschedule within policy | High | Old slot is released and new slot reserved atomically |
| FR-08 | Cancel and calculate refund | High | Status and refund amount follow policy; patient is notified |
| FR-09 | Send push/SMS reminders | Medium | Reminder contains correct appointment details and no unnecessary health data |
| FR-10 | View/download prescription | High | Only authorized patient can access the document |
| FR-11 | Manage profile and logout | Medium | Changes persist; logout invalidates the session |
| FR-12 | Handle emergency appointment request | Critical | Clear availability/fallback is shown without silent failure |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-01 | Primary screens should load within 3 seconds on stable 4G under normal load. |
| NFR-02 | The app should recover safely from network loss, calls, backgrounding and process restart. |
| NFR-03 | Support defined Android/iOS versions, screen sizes and orientations. |
| NFR-04 | Sensitive data must use secure transport, masked logs and authorization controls. |
| NFR-05 | Core journeys should support screen readers, scalable text, adequate contrast and large touch targets. |
| NFR-06 | English and Tamil text should render without clipping; dates/times must respect locale and timezone. |

## Assumptions

- A staging API, test accounts, payment sandbox and seeded database will be supplied.
- OTP may use a test bypass only in an authorized non-production environment.
- Actual supported OS versions and cancellation policy are confirmed before execution.

