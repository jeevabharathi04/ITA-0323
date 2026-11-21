# Task 03: Runtime Environment Analysis — Dalvik (DVM) vs Android Runtime (ART)

## 1. Evolution of the Android Virtual Machine

```text
Dalvik VM (Android 1.0 - 4.4):
  [.java Source] ──> [javac] ──> [.class] ──> [dx tool] ──> [.dex] 
                                                              │
                                            (Runtime JIT Compilation on Mobile CPU)
                                                              ▼
                                                     [Native Machine Code]

Android Runtime ART (Android 5.0+):
  [.java Source] ──> [D8/R8] ──> [.dex] ──> [Profile-Guided AOT + JIT (dex2oat)]
                                                              │
                                            (Pre-compiled during install & idle charging)
                                                              ▼
                                                [Optimized .oat ELF Native Code]
```

### Key Differences & Trade-offs:
1. **Compilation Paradigm:**
   - **Dalvik:** Just-in-Time (JIT) interpreter. Every time an app runs, methods are compiled in RAM on the fly, consuming heavy CPU cycles and battery.
   - **ART (Hybrid):** Ahead-of-Time (AOT) compiles frequently used execution paths (profile-guided via Cloud Profiles) while device is idle and charging, creating native `.oat` files.
2. **Garbage Collection (GC):**
   - **Dalvik:** Stop-the-world GC pauses often exceeded $50\text{ to }100\text{ ms}$, causing visible UI stutter and frame drops ("jank").
   - **ART:** Generational Concurrent Copying (CC) GC with compacting heaps reduces pause time to under $2\text{ to }3\text{ ms}$, effortlessly maintaining 60/120 fps animations.
3. **Storage vs Performance Trade-off:**
   - ART pre-compilation increases app on-disk storage footprint by $20\text{ to }40\%$, but cuts app startup latency by half and reduces runtime RAM consumption.
