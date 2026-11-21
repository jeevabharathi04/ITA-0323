# Task B1: Instrumented Background Architecture Implementation

This package contains full, production-grade Java source code implementing the complete mobile background architecture:
- `DataSyncWorker.java`: Standalone background worker with exponential backoff and constraint checks.
- `LocationTrackingService.java`: Foreground service simulation with mock notification hooks and power-aware sensor polling.
- `NetworkMonitorReceiver.java`: BroadcastReceiver dynamically monitoring network transitions.
- `OfflineRepository.java`: Thread-safe in-memory cache simulating a persistent SQLite/Room database.
