# Task 06 (Q6): Real-World Multiple Access Deployment Decision Matrix

| Deployment Environment | Primary Performance Constraint | Best Technique | Engineering Justification |
| :--- | :--- | :--- | :--- |
| **1. Massive IoT Sensor Network (Smart Campus)** | Extreme battery life (10 years), massive concurrency, tiny sporadic packets. | **OFDMA / Narrowband-IoT (NB-IoT)** | Narrow subcarriers ($3.75/15\text{ kHz}$) maximize link budget without wasting power on full-carrier transmissions; eliminates high-rate synchronization overheads of CDMA. |
| **2. High-Speed Rail Corridor ($350\text{ km/h}$)** | Severe Doppler shift ($f_d = v f_c / c$), rapid channel aging, frequent handoffs. | **TDMA / SC-FDMA (Single-Carrier)** | High Doppler spread destroys OFDMA subcarrier orthogonality (Inter-Carrier Interference). TDMA or SC-FDMA preserves low Peak-to-Average Power Ratio (PAPR) and high Doppler resilience. |
| **3. High-Density Stadium Arena (25,000 users)** | Extreme spatial traffic density ($1,250\text{ Erlangs/km}^2$). | **SDMA + OFDMA (Massive MIMO)** | Spatial multiplexing allows multi-user beamforming across 64+ antenna elements, reusing full subcarrier blocks 8-16 times simultaneously in distinct angular directions. |
| **4. Deep Rural Large-Cell Coverage ($R > 15\text{ km}$)** | Extreme path loss, low subscriber density, large delay spread. | **FDMA / Wideband-CDMA** | Narrow channels concentrate RF power for maximum range. Eliminates tight timing alignment required for large-cell OFDMA cyclic prefixes. |
