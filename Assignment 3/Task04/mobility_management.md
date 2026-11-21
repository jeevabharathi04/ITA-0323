# Task 04 (Q4): Mobile IP Micro-Mobility & Handoff Management

## 1. Limitations of Macro-Mobility (Mobile IP)
Standard Mobile IP is designed for macro-mobility (infrequent transitions across administrative domains).
When a user moves between access points on the same campus:
- Registering every micro-handoff with a distant Home Agent introduces high signaling overhead ($150\text{ to }300\text{ ms}$ latency).
- Result: Severe packet drops and jitter in VoIP and real-time streaming sessions.

---

## 2. Micro-Mobility Protocols: Cellular IP & HAWAII
1. **Cellular IP:**
   - Separates local handoffs from global registrations.
   - Nodes send small control dummy packets toward a Gateway Router (GW).
   - Intermediate routers cache routing state dynamically based on uplink packets, establishing soft-state return paths without Mobile IP registration.
2. **HAWAII (Handoff-Aware Wireless Access Internet Infrastructure):**
   - Retains the mobile host's CoA while moving within the domain.
   - Path-update messages dynamically splice routing entries at the crossover router.
