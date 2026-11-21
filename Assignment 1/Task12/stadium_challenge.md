# Task 12: Day-4 Design Challenge — Event Surge Adaptation

## 1. Impact Analysis of Stadium Surge
- **Event Scope:** Convocation / Inter-University Sports Event.
- **Attendees:** $25,000\text{ attendees}$ concentrated inside a $1\text{ km}^2$ stadium zone for $4\text{ hours}$.
- **Traffic Intensity:** $0.05\text{ Erlang/attendee}$ (double normal due to live video streaming, social media uploads, and calls).
- **Total Surge Demand:**
  $$A_{\text{stadium}} = 25,000 \times 0.05 = 1,250\text{ Erlangs inside } 1\text{ km}^2!$$

### Deficit of Baseline Unmodified Design:
In the baseline design, a single macrocell covers $\approx 1.5\text{ km}^2$, offering at most $56.4\text{ Erlangs}$.
- **Carried Traffic:** $56.4\text{ Erlangs}$
- **Unserved Traffic:** $1,250 - 56.4 = 1,193.6\text{ Erlangs}$
- **Blocking Probability:** $P_b > 95.4\%$. The network would suffer complete blackout!

---

## 2. Decision: MODIFY & REDESIGN (Dynamic Hybrid Overlay)

Permanent uniform cell splitting across the township would be economically absurd for a bi-weekly 4-hour event. The optimal engineering solution is a **Modular Event Overlay Deployment**:

```text
Stadium Zone Adaptive Architecture:
  ├── 1. Cell on Wheels (COW) Temporary Deployments
  │     └── 4 portable COWs parked at stadium cardinal quadrants.
  │     └── Micro-sectorized 60° antennas with 10 dB down-tilt.
  │
  ├── 2. Dynamic Channel Borrowing & Dedicated Event Carrier Pool
  │     └── Reserve 2 dedicated carriers (16 time-slots) from township periphery.
  │     └── Extreme antenna down-tilt (12°) restricts signal footprint strictly to stadium bowl.
  │
  ├── 3. Wi-Fi 6 / Small Cell Offload (High-Density CBRS/Unlicensed)
  │     └── 60 distributed high-capacity Wi-Fi 6 access points offload 70% of data traffic (875 Erlangs).
  │     └── Cellular network handles remaining 375 voice/high-priority Erlangs.
  │
  └── 4. Capacity Verification:
        └── 4 COWs × 4 sectors = 16 sectors.
        └── Each sector carries 24 channels = 15.3 Erlangs @ 2% GoS.
        └── Total cellular capacity = 16 × 15.3 = 244.8 Erlangs.
        └── With Wi-Fi offload, total capacity = 244.8 + 875 = 1,119.8 Erlangs.
        └── Blocking probability restored to Pb <= 2.1%.
```
