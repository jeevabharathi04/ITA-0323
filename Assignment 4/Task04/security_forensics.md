# Task 04: Mobile Security Forensics & Sandboxing

## 1. Mobile Threat Vectors & Attack Surfaces

### A. Implicit Intent Hijacking
- **Vulnerability:** When an application transmits an Intent without explicitly specifying a target Component Name (`setComponent()` or `setClass()`), the OS broadcasts it to all installed apps matching the Intent Filter.
- **Exploitation:** Malicious malware registers a high-priority Intent Filter for sensitive actions (e.g., `SEND_PAYMENT`) and intercepts user credentials.
- **Remediation:** Always use **Explicit Intents** for intra-app communication, or declare `android:exported="false"` in the Manifest for all internal activities and receivers.

### B. PendingIntent Mutable Flag Exploitation
- **Vulnerability:** Prior to Android 12, `PendingIntent` instances were mutable by default. A recipient malicious app could mutate the wrapped Intent's extras or target action before triggering it with the sender's elevated permissions!
- **Remediation:** Enforce `PendingIntent.FLAG_IMMUTABLE` on all pending intents.

### C. Permission Escalation & Confused Deputy
- Unprotected `ContentProvider` components leaking internal SQLite databases to third-party applications lacking read permissions.
