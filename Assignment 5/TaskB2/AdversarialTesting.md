# Task B2: Adversarial Workload Engineering & Stress Testing

## 1. Adversarial Stress Scenarios
To certify mobile software robustness before deployment:
1. **Network Flapping Chaos:** Toggling cellular connection between Connected, Disconnected, and Captive Portal every 500 ms while 50 background sync jobs are running.
2. **Low-Memory Killer (LMK) Simulation:** Rapidly allocating native memory to trigger `onTrimMemory(TRIM_MEMORY_RUNNING_CRITICAL)`.
3. **Database Concurrency Contention:** 20 concurrent threads reading and writing to the local cache simultaneously to verify zero deadlocks.
