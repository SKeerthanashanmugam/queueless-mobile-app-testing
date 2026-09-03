# Device and Network Matrix

Confirm supported versions with the product owner before execution.

| Tier | Platform/device profile | OS | Screen | Execution |
|---|---|---|---|---|
| Primary | Mid-range Android physical device | Android 15 | ~6.4 in | Full regression |
| Primary | Pixel emulator | Android 14 | 1080×2400 | Smoke + automation |
| Secondary | Low-memory Android/emulator | Android 12 | 720×1600 | Smoke/resilience |
| Secondary | iPhone simulator | iOS 18 | 6.1 in | Smoke/UI |
| Secondary | iPhone SE simulator | iOS 17 | 4.7 in | Layout/accessibility |
| Deferred | Physical iPhone | Supported current iOS | Representative | Push/camera/hardware validation |

## Network coverage

| ID | Condition | Focus |
|---|---|---|
| NET-01 | Stable Wi-Fi | Baseline |
| NET-02 | Stable 4G/5G | Normal mobile use |
| NET-03 | Throttled 3G/high latency | Loaders, timeouts and duplicate taps |
| NET-04 | Offline before action | Clear error and retry |
| NET-05 | Drop after payment submission | Idempotent reconciliation |
| NET-06 | Wi-Fi to mobile-data switch | Session and transaction continuity |

## Interruption coverage

Incoming call, SMS/push overlay, screen lock/unlock, Home/background/foreground, orientation change, low-battery mode, permission denial, process kill and device restart.

