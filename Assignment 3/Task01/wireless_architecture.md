# Task 01 (Q1): Wireless Network Architecture & 802.11 MAC Analysis

## 1. 802.11 Topology Architectures
- **Infrastructure Basic Service Set (BSS):** Centrally coordinated by an Access Point (AP). All traffic flows through the AP. Supports integration into wired backbones via the Distribution System (DS) to form an Extended Service Set (ESS).
- **Independent Basic Service Set (IBSS / Ad-Hoc):** Peer-to-peer network operating without any centralized coordinator. Nodes discover neighbors and self-organize dynamically.

---

## 2. Fundamental Wireless MAC Challenges & Solutions

### A. Hidden Terminal Problem
- **Scenario:** Node $A$ and Node $C$ cannot hear each other due to distance/obstacles, but both can communicate with intermediate Node $B$.
- **Failure:** Both $A$ and $C$ sense the channel as idle simultaneously and transmit to $B$, resulting in catastrophic collision at $B$.
- **Solution (CSMA/CA with RTS/CTS):**
  1. $A$ transmits a small **Request to Send (RTS)** frame to $B$.
  2. $B$ responds with a broadcast **Clear to Send (CTS)** frame containing the expected transmission duration.
  3. $C$ overhears the CTS and sets its **Network Allocation Vector (NAV)**, deferring transmission until $A$'s frame is completed.

### B. Exposed Terminal Problem
- **Scenario:** Node $B$ is transmitting to $A$. Node $C$ wants to transmit to an unrelated Node $D$.
- **Failure:** $C$ senses $B$'s transmission, falsely concludes the medium is busy, and unnecessarily defers, reducing spatial throughput.
- **Solution:** Directional antennas and dual-channel RTS/CTS protocols that distinguish transmitter carrier sensing from receiver vulnerability.
