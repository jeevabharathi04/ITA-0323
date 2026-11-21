# Task 07: Solution of Recurrence and Engineering Interpretation

## 1. Closed-Form Derivation via Repeated Substitution

Starting from the uniform recurrence:
$$M_k = 4 M_{k-1} = 4(4 M_{k-2}) = 4^k M_0$$
$$C_k = 4^k C_0$$
$$P_k = 2^{-n k} P_0$$

### Derivation of Required Rounds $k$ for Target Demand $D_{\text{target}}$:
To satisfy subscriber demand $D_{\text{target}}$:
$$C_k \ge D_{\text{target}} \implies 4^k C_0 \ge D_{\text{target}}$$
$$4^k \ge \frac{D_{\text{target}}}{C_0}$$
Taking base-4 logarithms:
$$k = \left\lceil \log_4\left( \frac{D_{\text{target}}}{C_0} \right) \right\rceil = \left\lceil \frac{\ln(D_{\text{target}} / C_0)}{\ln 4} \right\rceil$$

---

## 2. Quantitative Evaluation for University Township

- **Base Layout ($k=0$):** $R_0 = 1.0\text{ km}$, $M_0 = 5\text{ cells}$, $P_0 = 20\text{ W}$.
  Base Capacity ($N=4$, $120^\circ$ sectoring): $C_0 = 5 \times 56.4 = 282\text{ Erlangs} \implies 11,280\text{ users}$.

- **Target Demand ($100,000$ users):**
  $$D_{\text{target}} = 100,000 \times 0.025 = 2,500\text{ Erlangs}$$
  $$k = \left\lceil \log_4\left( \frac{2,500}{282} \right) \right\rceil = \lceil \log_4(8.865) \rceil = \lceil 1.573 \rceil = 2\text{ rounds}$$

### Network State Progression:
| Splitting Round $k$ | Cell Radius $R_k$ | Total Cells $M_k$ | Transmit Power ($n=3.5$) | Erlang Capacity | Max Supported Users |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$k = 0$ (Initial)** | $1.000\text{ km}$ | $5$ | $20.00\text{ W}$ ($43.0\text{ dBm}$) | $282$ | $11,280$ |
| **$k = 1$** | $0.500\text{ km}$ | $20$ | $1.77\text{ W}$ ($32.5\text{ dBm}$) | $1,128$ | $45,120$ |
| **$k = 2$** | $0.250\text{ km}$ | $80$ | $0.16\text{ W}$ ($21.9\text{ dBm}$) | $4,512$ | $180,480$ (Exceeds goal) |

---

## 3. Mobility and Handoff Impact

While cell splitting solves capacity, it imposes severe mobility penalties:
1. **Mean Cell Residence Time:** $T_{\text{dwell}} \propto R_k$.
   For an on-campus vehicle moving at $v = 36\text{ km/h} = 10\text{ m/s}$:
   - At $R = 1.0\text{ km}$, $T_{\text{dwell}} \approx 100\text{ seconds}$.
   - At $R = 0.25\text{ km}$, $T_{\text{dwell}} \approx 25\text{ seconds}$.
2. **Handoff Rate Growth:** $\lambda_{\text{ho}} \propto 1/R_k = 2^k$.
   Handoff execution frequency increases by $4\times$, requiring high-speed fiber backhaul and localized Base Station Controller (BSC) handoff processing to prevent call drops.
