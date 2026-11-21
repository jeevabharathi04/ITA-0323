# Task A1: Constraint-Aware Intent & Service Architecture

## 1. Background Execution Taxonomy in Modern Android

```text
Background Work Classification:
  ├── 1. Immediate / User-Visible Task ──> Foreground Service
  │     └── Requires persistent Status Bar notification.
  │     └── Examples: Turn-by-turn navigation, active audio playback.
  │
  ├── 2. Deferrable / Guaranteed Task ──> WorkManager (Jetpack)
  │     └── Survives app death and system reboots.
  │     └── Executes when battery and network constraints are satisfied.
  │     └── Examples: Telemetry batch upload, local database compaction.
  │
  └── 3. Short / Asynchronous In-Memory ──> Kotlin Coroutines / ThreadPool
        └── Bound strictly to component lifecycle (ViewModelScope / LifecycleScope).
        └── Cancelled automatically when user exits the Activity.
```

---

## 2. Decision Tree for Service Selection
1. **Does the task require immediate user visibility?**
   - **YES:** Use a **Foreground Service** (`startForegroundService()`) with a valid `foregroundServiceType` (e.g., `location` or `mediaPlayback`).
   - **NO:** Proceed to Step 2.
2. **Must the task run even if the user leaves the app or restarts the device?**
   - **YES:** Use **WorkManager** with an exponential backoff policy.
   - **NO:** Use in-memory asynchronous threads (`ThreadPoolExecutor` or Coroutines).
