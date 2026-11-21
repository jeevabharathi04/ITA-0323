# Task 07 (Q7 - Day 4): Diagnose, Redesign, and Validate

## 1. Architectural Diagnosis of Impaired Multiple Access System
An initial field audit identified severe network degradation under concurrent voice and bursty academic file transfers:
1. **PAPR Degraded Cell Edge:** Uplink transmissions in pure OFDMA suffered high Peak-to-Average Power Ratio, forcing power amplifiers into saturation and draining mobile batteries rapidly.
2. **Channel Starvation from Static Allocation:** Fixed time-slot assignment left 80% of bandwidth idle during quiet periods, while dropping telemetry packets during surges.

---

## 2. Redesign Blueprint: Hybrid SC-FDMA / OFDMA Dual-Tier Scheduler
- **Uplink:** Adopt **Single-Carrier FDMA (SC-FDMA)** using DFT-spread OFDM. Reduces PAPR by $3.5\text{ dB}$, enabling mobiles to transmit at maximum amplifier efficiency and extending campus battery life.
- **Downlink:** Retain **OFDMA with Proportional Fair Scheduling** to maximize multi-user diversity across wideband carriers.
- **Dynamic Access Grant:** Replaced fixed TDMA slots with contention-based random access preamble (PRACH) transitioning to scheduled OFDMA resource blocks.
