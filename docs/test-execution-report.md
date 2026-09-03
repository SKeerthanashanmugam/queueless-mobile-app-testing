# Mobile Test Execution Report

## Execution Details

| Field | Value |
|---|---|
| Build/version | QueueLess Android Debug Build 1.0 |
| Environment | Local QA |
| Execution date | 2026-09-04 |
| Tester | Keerthana S |
| Device/OS | OPPO CPH2495 / Android 15 |

## Execution Results

| Metric | Count |
|---|---:|
| Planned | 70 |
| Executed | 9 |
| Passed | 9 |
| Failed | 0 |
| Blocked | 0 |
| Not run | 61 |

## Executed Test Cases

| Test Case | Area | Result |
|---|---|---|
| TC-006 | Valid mobile number and OTP login | Passed |
| TC-007 | Invalid mobile-number validation | Passed |
| TC-014 | Search doctor by specialty | Passed |
| TC-016 | No-result search behaviour | Passed |
| TC-020 | Doctor profile information | Passed |
| TC-023 | Book available appointment | Passed |
| TC-030 | Successful test payment | Passed |
| TC-041 | Cancel appointment | Passed |
| TC-054 | Logout and session protection | Passed |

## Execution Notes

The selected smoke and critical-path test cases were manually executed on a physical OPPO CPH2495 running Android 15. All nine executed test cases passed. Screenshots are stored in `evidence/screenshots`.

The remaining 61 cases are not yet executed and are retained for future regression, compatibility, accessibility, network and interruption testing.

## Android Build and Automated Verification

| Verification | Command | Result |
|---|---|---|
| Android unit tests | `gradlew.bat test` | Passed — BUILD SUCCESSFUL |
| Physical-device instrumented tests | `gradlew.bat connectedAndroidTest` | Passed — BUILD SUCCESSFUL |
| Application installation and launch | Android Studio Run on OPPO CPH2495 | Passed |

The QueueLess Android application was compiled, installed and launched on a physical OPPO CPH2495 device. Gradle unit tests and connected instrumented tests completed successfully.