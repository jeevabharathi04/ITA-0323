# Task 02 (Q2): FDMA vs TDMA Under Bursty Traffic & Voice

## 1. Mechanism Comparison

### Frequency Division Multiple Access (FDMA):
- Spectrum is divided into narrow frequency carriers (e.g., $30\text{ kHz}$ or $200\text{ kHz}$).
- A user is allocated a dedicated frequency for the entire duration of the call/session.
- If the user is silent (voice inactivity / bursty telemetry gaps), the spectrum sits completely idle, wasting capacity.

### Time Division Multiple Access (TDMA):
- The entire channel bandwidth is shared dynamically in cyclically repeating time-frames.
- Each frame is subdivided into $N_{\text{slots}}$ time-slots (e.g., 8 slots in GSM).
- Users transmit in short, high-rate bursts during their assigned slot.
- Enables dynamic time-slot assignment: a bursty telemetry device can be allocated 1 slot every 10 frames, while video gets 4 slots per frame.

---

## 2. Quantitative Queueing & Delay Under Bursty IoT Telemetry

For $K$ IoT sensor nodes transmitting sporadic data bursts:
- **In FDMA:** Each node has a dedicated micro-carrier. Average waiting time $W_{\text{FDMA}} = 0$, but spectral utilization is $< 2\%$. Number of supported devices is strictly hard-limited by carrier count.
- **In TDMA:** Packet arrival is Poisson with rate $\lambda$. Packets queue until the designated time slot.
  Average transmission delay:
  $$D_{\text{TDMA}} = \frac{T_{\text{frame}}}{2} + \frac{\lambda \cdot \mathbb{E}[S^2]}{2(1 - \rho)} + T_{\text{slot}}$$
  TDMA supports $10\times$ more IoT nodes within the same bandwidth due to dynamic statistical multiplexing.
