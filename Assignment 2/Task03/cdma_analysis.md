# Task 03 (Q3): CDMA Orthogonality, Spreading & Near-Far Problem

## 1. Orthogonal Code Theory & Walsh-Hadamard Codes
In Direct-Sequence Code Division Multiple Access (DS-CDMA), all users transmit simultaneously over the exact same frequency band. Separation is achieved by assigning each user an orthogonal pseudo-random code sequence $C_k(t)$.

For any two Walsh code sequences $W_i, W_j$ of length $L$:
$$\frac{1}{L} \sum_{m=1}^L W_i[m] W_j[m] = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

### Transmission & Despreading:
If user $k$ transmits data bit $b_k \in \{-1, +1\}$, the composite received signal at the base station is:
$$R(t) = \sum_{k=1}^K \sqrt{P_k} \, b_k \, C_k(t) + n(t)$$
Multiplying by the desired user's code $C_1(t)$ over one symbol period $T_b$:
$$y_1 = \frac{1}{T_b} \int_0^{T_b} R(t) C_1(t) \, dt = \sqrt{P_1} b_1 + \sum_{k=2}^K \sqrt{P_k} b_k \left( \frac{1}{T_b} \int_0^{T_b} C_k(t) C_1(t) dt \right) + n_1$$
Under perfect code orthogonality, the cross-correlation summation evaluates strictly to **zero**, completely recovering bit $b_1$!

---

## 2. The Near-Far Problem & Power Control
In the uplink, if a nearby mobile $M_1$ is at $100\text{ m}$ from the base station and a distant mobile $M_2$ is at $2,000\text{ m}$, the uncompensated received power difference is:
$$\Delta P_{\text{rx}} = \left( \frac{2000}{100} \right)^4 = 20^4 = 160,000 \implies 52\text{ dB difference!}$$

Even with a high spreading factor (processing gain $G = 128 \approx 21\text{ dB}$), cross-correlation leakage from the non-orthogonal multipath of $M_1$ will completely drown out the desired signal from $M_2$.

### Solution: Fast Closed-Loop Power Control
- Base station measures received SNR 800 to 1,500 times per second.
- Transmits 1-bit Transmit Power Control (TPC) commands (UP / DOWN by $0.5\text{ dB}$ or $1.0\text{ dB}$) to ensure all mobile signals arrive at the base station antenna within $\pm 0.5\text{ dB}$ of each other.
