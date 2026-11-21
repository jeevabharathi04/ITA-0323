# Task 04: Best, Average, and Worst-Case Behaviour

## 1. Spatial Variation of SIR Across Cell Geometry

The Signal-to-Interference Ratio is not static; it varies continuously based on user location relative to the serving and co-channel base stations.

```text
Cell Geometry Locations:
  [BS Center: r = 0] ─────────── [Mid-Cell: r = R/2] ─────────── [Cell Corner: r = R]
      Best Case                     Average Case                     Worst Case
   SIR > 35 dB                      SIR ≈ 22 dB                     SIR ≈ 14-18 dB
```

### Case 1: Best-Case Spatial SIR (Mobile Near Base Station)
- **Location:** Mobile within distance $r \le 0.1 R$ from serving tower.
- **Serving Power:** $C \propto (0.1 R)^{-n} = 10^n R^{-n}$.
- **Interferers:** Distance to co-channel cells is $D_k \ge D - 0.1 R \approx D$.
- **Resulting SIR:**
  $$\text{SIR}_{\text{best}} \approx \frac{(0.1 R)^{-n}}{6 D^{-n}} = \frac{10^n}{6} Q^n$$
  For $n = 3.5, N = 7$ ($Q = 4.58$): $\text{SIR}_{\text{best}} > 45\text{ dB}$.
  Zero co-channel interference impact; reception is thermal-noise limited.

### Case 2: Average-Case Spatial SIR (Mid-Cell Region)
- **Location:** Distributed over the mid-annulus area ($0.4 R \le r \le 0.7 R$).
- **Geometric Expectation:** Median path loss $\mathbb{E}[r^{-n}]$ across the hexagonal disc.
- **Resulting SIR:** Evaluates to approximately $4\text{ to }6\text{ dB}$ higher than the corner worst-case. For $N = 7, n = 3.5$, average $\text{SIR} \approx 21.8\text{ dB}$.

### Case 3: Worst-Case Spatial SIR (Cell Boundary / Tri-Cell Vertex)
- **Location:** Mobile located at the vertex (corner) of the hexagon: $r = R$.
- **Interferer Geometry:** Two of the first-tier co-channel base stations are closer than $D$:
  $$D_1 \approx D - R, \quad D_2 \approx D - R, \quad D_3, D_4 \approx D, \quad D_5, D_6 \approx D + R$$
- **Exact Summed Interference:**
  $$I_{\text{worst}} = P_t K_0 \left[ 2(D-R)^{-n} + 2 D^{-n} + 2(D+R)^{-n} \right]$$
  $$\text{SIR}_{\text{worst}} = \frac{R^{-n}}{2(D-R)^{-n} + 2D^{-n} + 2(D+R)^{-n}} = \frac{1}{2(Q-1)^{-n} + 2Q^{-n} + 2(Q+1)^{-n}}$$
- **Numerical Example ($N=7, Q=4.58, n=4$):**
  - Standard equidistant formula: $\text{SIR} = (4.58)^4 / 6 = 73.35 \implies 18.65\text{ dB}$.
  - Worst-case exact vertex formula:
    $$2(3.58)^{-4} + 2(4.58)^{-4} + 2(5.58)^{-4} = 0.01217 + 0.00454 + 0.00206 = 0.01877$$
    $$\text{SIR}_{\text{exact-worst}} = \frac{1}{0.01877} = 53.27 \implies 17.26\text{ dB} \quad (1.4\text{ dB degradation!})$$

---

## 2. Traffic-Load Temporal Dynamics (Off-Peak vs Busy-Hour)

| Traffic Regime | Time Window | Traffic / User | System Behavior & Grade of Service |
| :--- | :--- | :--- | :--- |
| **Off-Peak** | 02:00 – 06:00 | $0.002\text{ Erlang}$ | $P_b \ll 0.0001$. Available channels idle; full bitrates available. |
| **Average Daytime** | 10:00 – 16:00 | $0.015\text{ Erlang}$ | $P_b \approx 0.003$ ($0.3\%$). High voice clarity, zero queuing delay. |
| **Busy-Hour** | 17:00 – 19:00 | $0.025\text{ Erlang}$ | Operates precisely at design target: $P_b = 0.020$ ($2.0\%$). |
| **Event Surge (Day 4)** | 14:00 – 18:00 (Stadium) | $0.050\text{ Erlang}$ | Unmodified network enters severe congestion: $P_b > 68\%$. |

---

## 3. Impact of Shadow Fading (Log-Normal Distribution)

In real campus environments, buildings and terrain induce log-normal shadowing:
$$P_{r,\text{dB}} = P_{\text{tx,dB}} - 10n \log_{10}(d/d_0) + X_\sigma$$
where $X_\sigma \sim \mathcal{N}(0, \sigma^2)$ with shadow standard deviation $\sigma \in [6, 8]\text{ dB}$.

Because carrier power $C$ and each interferer $I_k$ shadow independently, instantaneous SIR follows a Gaussian distribution in the dB domain:
$$\text{SIR}_{\text{dB}} \sim \mathcal{N}\left( \mu_{\text{SIR}}, \sigma_{\text{eff}}^2 \right), \quad \sigma_{\text{eff}} = \sqrt{\sigma_C^2 + \sigma_I^2}$$
**Outage Probability ($P_{\text{out}}$):**
$$P_{\text{out}} = P(\text{SIR} < \gamma_{\text{threshold}}) = Q\left( \frac{\mu_{\text{SIR}} - \gamma_{\text{threshold}}}{\sigma_{\text{eff}}} \right)$$
To maintain $95\%$ edge availability, a fade margin of $1.645 \sigma_{\text{eff}} \approx 8\text{ to }12\text{ dB}$ must be engineered into the baseline reuse planning.
