# Task 05: Scaling and Sensitivity Analysis

## 1. Proportionality Laws in Cellular Networks

The governing equations yield fundamental scaling laws:

1. **Cell Count Scaling:**
   $$M \propto \frac{1}{R^2}$$
   Halving cell radius quadruples base station site density.

2. **Per-Cell Capacity Scaling:**
   $$K \propto \frac{1}{N}$$
   Channels per cell are strictly inversely proportional to cluster size.

3. **Interference Ratio Scaling:**
   $$\text{SIR} \propto N^{n/2}$$
   Sensitivity to cluster size is amplified exponentially by the path-loss exponent $n$.

4. **Total Network Capacity:**
   $$C_{\text{total}} \propto M \times K \propto \frac{1}{R^2 N}$$

---

## 2. Sensitivity to Propagation Exponent $n$ ($n = 2.5 \to 4.0$)

The path-loss exponent heavily dictates achievable cluster sizes:

| Path-Loss Exponent $n$ | Environment Description | $\text{SIR}_{\text{omni}}(N=7)$ | $\text{SIR}_{120^\circ}(N=4)$ | Feasible Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **$n = 2.5$** | Open sports grounds / flat rural campus | $10.9\text{ dB}$ (Fails $15\text{ dB}$) | $11.8\text{ dB}$ (Fails $15\text{ dB}$) | Requires $N=12$ or $60^\circ$ sectoring |
| **$n = 3.0$** | Suburban campus / light vegetation | $14.1\text{ dB}$ (Borderline) | $15.5\text{ dB}$ (Meets $15\text{ dB}$) | $N=4$ Sectored or $N=7$ Omni |
| **$n = 3.5$** | Mixed academic & hostel blocks | $16.9\text{ dB}$ (Robust) | $18.8\text{ dB}$ (Robust) | $N=4$ Sectored is optimal |
| **$n = 4.0$** | Dense multi-story concrete buildings | $18.7\text{ dB}$ (High margin) | $21.5\text{ dB}$ (High margin) | $N=3$ Sectored feasible |

**Key Takeaway:** As the campus becomes more densely built up, $n$ increases from $2.5$ to $4.0$, which drastically attenuates distant interfering signals. Paradoxically, higher path loss **improves cellular SIR**, enabling more aggressive frequency reuse!

---

## 3. Break-Even Scale Analysis

When subscribers scale from $1,000$ to $100,000+$, a single strategy cannot remain optimal:

```text
Capacity Ceiling of Macrocell Strategy (N=7, Omni, R=1.0 km):
  └── 48 channels/cell @ 2% GoS = 36.8 Erlangs/cell.
  └── 5 cells across 12 km² = 184 Erlangs total.
  └── Subscriber Limit: 184 / 0.025 = 7,360 subscribers.
  └── Break-even Point 1: At 7,500 users, Strategy A fails. Must adopt Strategy B (Sectoring).

Capacity Ceiling of Sectored Strategy (N=4, 120° Sectoring, R=0.6 km):
  └── 28 channels/sector @ 2% GoS = 18.8 Erlangs/sector × 3 = 56.4 Erlangs/cell.
  └── 13 cells across 12 km² = 733.2 Erlangs total.
  └── Subscriber Limit: 733.2 / 0.025 = 29,328 subscribers.
  └── Break-even Point 2: At ~30,000 users, Strategy B reaches density limit. Must adopt Strategy C (Repeated Cell Splitting).
```
