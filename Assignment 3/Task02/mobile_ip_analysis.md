# Task 02 (Q2): Mobile IP Protocol & Mobility Management

## 1. Entities & Addressing in Mobile IP (RFC 5944)
1. **Mobile Node (MN):** Host that changes its point of attachment from one network to another while preserving ongoing TCP sessions.
2. **Home Agent (HA):** Router on the MN's home network that intercepts packets addressed to the MN's permanent Home Address and tunnels them.
3. **Foreign Agent (FA):** Router on the visited network providing routing services and advertising a **Care-of Address (CoA)**.
4. **Correspondent Node (CN):** Peer node communicating with the MN.

---

## 2. Triangular Routing & Route Optimization

```text
Standard Triangular Routing:
    [Correspondent Node CN] ─────────────────> [Home Agent HA]
              ▲                                      │
              │ (Direct Return)                      │ (IP-in-IP Encapsulated Tunnel)
              │                                      ▼
              └────────────────────────────── [Mobile Node MN (at FA)]
```

### Triangle Routing Inefficiency:
- Packets from CN must traverse the home network regardless of where CN and MN are physically located.
- If CN and MN are in the same foreign university room, packets still travel across the globe to HA and back!

### Route Optimization Solution (Binding Updates):
- HA sends a **Binding Update** to CN containing the MN's current CoA.
- CN caches this binding and tunnels subsequent packets directly to MN's CoA, bypassing HA completely.

---

## 3. Reverse Tunneling (RFC 3024)
- **Problem:** Many enterprise routers implement **Ingress Filtering** (RFC 2827): dropping packets whose source IP address does not match the local subnet prefix. Direct return packets from MN (carrying its Home Address as source) are dropped by visited border routers!
- **Solution (Reverse Tunnel):** FA encapsulates the MN's packets inside a reverse tunnel directed to HA. HA decapsulates the packets and routes them normally to CN.
