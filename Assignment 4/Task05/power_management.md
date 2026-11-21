# Task 05: Mobile Power Management & Battery Optimization

## 1. Android Power Optimization Mechanisms
To prevent rogue applications from draining mobile batteries:
1. **Doze Mode:**
   - Triggered when the device is stationary, screen off, and running on battery.
   - Restricts CPU wake locks, suspends network access, defers background alarms, and batches job executions into periodic maintenance windows.
2. **App Standby Buckets:**
   - Categorizes apps dynamically based on user engagement: `Active`, `Working Set`, `Frequent`, `Rare`, `Restricted`.
   - Apps in the `Rare` bucket have their background jobs throttled to once every 24 hours.
3. **The WakeLock Hazard:**
   - A `PARTIAL_WAKE_LOCK` forces the application processor (AP) to remain powered on even with the screen off. A leaked wake lock will drain a smartphone battery from $100\%$ to $0\%$ in under 4 hours.

---

## 2. Evolution of Scheduling APIs
```text
AlarmManager (Unconstrained, High Wakeups) 
    └──> JobScheduler (API 21: Batched on Wi-Fi/Charging)
            └──> WorkManager (Modern Jetpack Standard: Guaranteed, Constraint-Aware Execution)
```
