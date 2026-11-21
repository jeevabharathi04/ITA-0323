# Task A2: Concurrency & Synchronization Safety in Mobile

## 1. The Single-Threaded UI Rule & ANR Avoidance
- In Android, the Main Thread (UI Thread) processes user input events, draws views, and coordinates lifecycle callbacks.
- **Application Not Responding (ANR):** Triggered by the OS if the main thread is blocked for $> 5\text{ seconds}$ (or $> 10\text{ seconds}$ in a BroadcastReceiver).
- **Rule:** Never execute disk I/O, database queries, network sockets, or CPU-intensive math on the main thread!

---

## 2. Android Thread Communication: Looper, Handler, and MessageQueue

```text
Worker Thread                                            Main Thread (UI)
[Background Work]                                        [Looper / UI Thread]
        │                                                         ▲
        │ 1. handler.post(runnable)                               │ 3. Dispatches message
        ▼                                                         │    to Target Handler
[MessageQueue] ───────────────────────────────────────────────────┘
               2. Looper.loop() extracts messages sequentially
```
