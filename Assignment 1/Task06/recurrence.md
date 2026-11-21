# Task 06: Recurrence Formulation for Repeated Cell Splitting

## 1. Problem Formulation
When cell traffic density exceeds saturation, macrocells are split into microcells.
Let:
- $k \in \{0, 1, 2, \dots\}$ denote the splitting round index ($k=0$ is the un-split base layout).
- $R_k$ be the cell radius at round $k$.
- $M_k$ be the total cell count at round $k$.
- $C_k$ be the total system voice capacity (Erlangs) at round $k$.
- $P_k$ be the required base station transmit power at round $k$.

### Radius Reduction Rule:
In each splitting round, the cell radius is halved:
$$R_k = \frac{R_{k-1}}{2} = \frac{R_0}{2^k}$$

### Cell Area Relation:
$$A_k = \frac{3\sqrt{3}}{2} R_k^2 = \frac{A_{k-1}}{4} = \frac{A_0}{4^k}$$

---

## 2. Recurrence Relations

### A. Uniform Splitting (All cells split simultaneously)
Every cell of radius $R_{k-1}$ is replaced by 4 smaller cells of radius $R_k = R_{k-1}/2$:
$$M_k = 4 \cdot M_{k-1}, \quad \text{Base Case: } M_0 = \left\lceil \frac{A_{\text{total}}}{2.598 R_0^2} \right\rceil$$
$$C_k = 4 \cdot C_{k-1}, \quad \text{Base Case: } C_0 = M_0 \cdot A_{\text{cell}}$$

### B. Transmit Power Scaling:
To ensure the signal strength at the new boundary $R_k$ matches that of the old boundary $R_{k-1}$, and co-channel interference scales identically:
$$P_k \cdot R_k^{-n} = P_{k-1} \cdot R_{k-1}^{-n}$$
$$P_k = P_{k-1} \cdot \left( \frac{R_k}{R_{k-1}} \right)^n = P_{k-1} \cdot \left( \frac{1}{2} \right)^n = \frac{P_{k-1}}{2^n}$$
Base Case: $P_0 = 20\text{ Watts}$ ($43\text{ dBm}$).

### C. Selective Splitting (Fraction $\alpha_k$ of cells overloaded):
In reality, only cells covering hotspots (academic block, hostels) overload:
$$M_k = M_{k-1} + 3 \alpha_k M_{k-1} = M_{k-1}(1 + 3\alpha_k)$$
where $\alpha_k \in [0, 1]$ is the fraction of cells split in round $k$.
