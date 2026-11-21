# Task 06: Day-4 Design Challenge — Mission-Critical Field Operations Blueprint

## 1. Scenario: Campus Field Emergency & Inspection Dispatch
- University field officers and campus security units operate tablets across hazardous campus terrain with intermittent cellular connectivity, harsh battery constraints, and strict real-time telemetry requirements.

---

## 2. Resilient Architecture Specifications

```text
Mission-Critical Mobile Architecture:
  ├── 1. Data Layer (Offline-First Single Source of Truth)
  │     └── Room SQLite Database acts as the primary data store.
  │     └── Bidirectional sync engine uses vector clocks for optimistic conflict resolution.
  │
  ├── 2. Background Synchronization Layer
  │     └── Jetpack WorkManager with Exponential Backoff retry policy.
  │     └── Strict constraints: NetworkType.CONNECTED + BatteryNotLow.
  │
  ├── 3. Secure Inter-Process Communication
  │     └── Encrypted SQLite via SQLCipher.
  │     └── Inter-service communication via Explicit Intents with custom signature-level permissions.
  │
  └── 4. Power & Thermal Management Engine
        └── Adaptive GPS Duty Cycling: 1 Hz polling during active emergency, throttled to 0.01 Hz when stationary (fused accelerometer wakeups).
```
