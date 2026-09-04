# QueueLess API Test Execution Report

## Execution Details

| Field | Value |
|---|---|
| Project | QueueLess – Smart Hospital Appointment System |
| Test type | REST API functional and security testing |
| Tool | Postman |
| Environment | QueueLess Local QA |
| Execution date | 2026-09-04 |
| Tester | Keerthana S |
| API server | Python local reference API |
| Base URL | http://127.0.0.1:8000/api |

## Execution Summary

| Metric | Result |
|---|---:|
| API requests executed | 7 |
| Test assertions executed | 11 |
| Passed | 11 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |
| Average response time | 8 ms |
| Total duration | 1.505 seconds |

## Endpoints Tested

| Method | Endpoint | Validation | Result |
|---|---|---|---|
| GET | `/health` | Status code and response time | Passed |
| POST | `/auth/otp/request` | Request accepted without exposing OTP | Passed |
| GET | `/doctors?specialty=Cardiology` | Status code and JSON response | Passed |
| GET | `/doctors/D001/slots` | Available slots returned | Passed |
| POST | `/appointments` | Appointment created successfully | Passed |
| GET | `/appointments/APT-001` | Correct appointment returned | Passed |
| GET | `/appointments/APT-001/prescription` | Unauthenticated access rejected with 401 | Passed |

## Security Validation

The unauthorized prescription request returned HTTP `401 Unauthorized`. This is the expected result and confirms that protected patient information cannot be accessed without authentication.

## Evidence

Postman collection-run screenshot:

`evidence/screenshots/API-Postman-Collection-Run.png`

## Conclusion

All 11 Postman assertions passed with no failures or execution errors. The tested API flows covered service health, OTP requests, doctor search, slot retrieval, appointment creation, appointment retrieval, and unauthorized-access protection.