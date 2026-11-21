# Assignment 5 (CO5): Android Application Features & Performance Engineering

This directory contains the background execution architectures, thread safety analyses, adversarial stress testing harnesses, and graphics optimization strategies for **CO5: Mobile Background Services, Performance Optimization, and System Engineering**.

---

## 📑 Tasks Index

| Task Folder | Focus Area | Deliverables / Code |
| :--- | :--- | :--- |
| [TaskA1/](TaskA1/IntentServiceArchitecture.md) | Service Architecture | Foreground vs Background Services vs WorkManager decision tree. |
| [TaskA2/](TaskA2/ConcurrencySafety.md) | Thread Safety & ANRs | UI thread single-thread rule, Handler/Looper, and ANR prevention. |
| [TaskA3/](TaskA3/BackgroundPatterns.md) | Mobile Background Patterns | Offline-First Repository pattern and exponential backoff with jitter. |
| [TaskA4/](TaskA4/ProcessingTradeoffs.md) | Local vs Cloud Processing | Mathematical computation offloading energy trade-off model. |
| [TaskA5/](TaskA5/ApproximateOptimization.md) | Approximate Optimization | Heuristic battery conservation, GPS duty cycling, downsampling. |
| [TaskB1/](TaskB1/) | Background Suite Implementation | Java implementation: `DataSyncWorker`, `LocationTrackingService`, `OfflineRepository`. |
| [TaskB2/](TaskB2/) | Adversarial Workload Testing | Network flapping, concurrency stress test: `AdversarialLoadSimulator.java`. |
| [TaskB3/](TaskB3/GraphicsOptimization.md) | UI & 60/120 FPS Budgeting | Overdraw elimination, ConstraintLayout flattening, ViewStub. |
| [TaskB4/](TaskB4/FinalEngineeringDecision.md) | Production Decision Report | Final architecture sign-off, telemetry spec, and Android 14+ compliance. |
