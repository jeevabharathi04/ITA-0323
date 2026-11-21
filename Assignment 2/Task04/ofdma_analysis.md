# Task 04 (Q4): OFDMA Subcarrier Allocation & Channel-Aware Scheduling

## 1. Principles of OFDMA (Orthogonal Frequency Division Multiple Access)
- Wideband channel is divided into hundreds of narrow, orthogonal subcarriers ($15\text{ kHz}$ spacing in LTE/5G).
- Orthogonality condition: subcarrier spacing $\Delta f = 1/T_s$, where $T_s$ is the symbol duration. Subcarrier spectral peaks coincide with nulls of all neighboring subcarriers.
- Multipath delay spread immunity is guaranteed by appending a **Cyclic Prefix (CP)** longer than channel delay spread $\tau_{\text{max}}$, converting frequency-selective fading into flat fading per subcarrier.

---

## 2. Multi-User Diversity & Opportunistic Scheduling
In a wireless environment, different users experience independent frequency-selective fading dips at different subcarriers:
- **Proportional Fair (PF) Scheduling:**
  Schedules user $i$ on subcarrier $k$ that maximizes the ratio of instantaneous achievable rate $R_{i,k}(t)$ to past average throughput $\bar{R}_i(t)$:
  $$i^* = \arg\max_i \left( \frac{R_{i,k}(t)}{\bar{R}_i(t)} \right)$$
- Exploits multi-user diversity: the probability that a subcarrier is in a deep fade for *all* users approaches zero as user count grows.
