# Task A3: Mobile Background Design Patterns

## 1. The Offline-First Repository Pattern
The application UI should never query the remote network directly. Instead, it subscribes to a reactive local cache (SQLite / Room):

```text
[UI / View] <====== Reactive Flow / LiveData ====== [Local Room DB Cache]
                                                           ▲
                                                           │ (Background Sync)
                                                           ▼
                                                 [Remote REST / Cloud API]
```

## 2. Exponential Backoff with Jitter
When retrying failed network requests, simple periodic retries create **Thundering Herd** server overloads.
The delay for retry attempt $n$ is:
$$T_{\text{retry}} = \min(T_{\text{max}}, T_{\text{base}} \cdot 2^n) + \text{random\_jitter}$$
