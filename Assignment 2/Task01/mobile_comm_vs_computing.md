# Task 01 (Q1): Mobile Communication vs Mobile Computing Audit

## 1. Technological Differentiation Matrix

| Attribute | Mobile Communication | Mobile Computing |
| :--- | :--- | :--- |
| **Primary Objective** | Bit-level data transmission across a wireless channel without corruption. | Execution of distributed stateful computations across mobile and edge/cloud nodes. |
| **Layer of Operation** | Physical (Layer 1) and Data Link / MAC (Layer 2). | Transport (Layer 4), Session (Layer 5), and Application (Layer 7). |
| **Core Challenges** | Multi-path fading, Doppler spread, path loss, co-channel interference, bit error rate (BER). | Context-awareness, battery energy preservation, intermittent connectivity, data synchronization. |
| **Metric of Success** | Signal-to-Interference Ratio (SIR), throughput (bps/Hz), spectral efficiency, latency. | Computation time, energy consumed per task, cache freshness, application responsiveness. |
| **Hardware Focus** | Antennas, RF transceivers, power amplifiers, DSP modulation engines. | Multi-core mobile SoC, neural processing units (NPU), flash storage, OS power management. |

---

## 2. Real-World Field Audit Analysis

In the university township scenario, an automated ambulance telemetry system requires both domains:
1. **Mobile Communication Domain:**
   - Establishing a robust 4G/5G radio bearer with sufficient SNR while moving at $80\text{ km/h}$.
   - Managing seamless inter-cell handoffs and packet scheduling over the air interface.
2. **Mobile Computing Domain:**
   - Onboard real-time compression of ECG signals and patient biometric telemetry.
   - Local decision algorithms determining whether to upload raw high-resolution video or distilled diagnostic alerts when cellular bandwidth drops.
   - Synchronizing patient vitals with hospital emergency room databases using optimistic conflict-resolution protocols.
