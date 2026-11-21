# Task 03: Mathematical Derivations of Capacity, Geometry, and Interference

## 1. Hexagonal Geometry & Tiling Relations

A regular hexagon with side length / radius $R$ (distance from center to any vertex) has an area given by summing 6 equilateral triangles:
$$A_{\text{cell}} = 6 \times \left( \frac{\sqrt{3}}{4} R^2 \right) = \frac{3\sqrt{3}}{2} R^2 \approx 2.598076 R^2$$

For a total service region of $A_{\text{total}} = 12\text{ km}^2$, the minimum number of cells $M$ is:
$$M(R) = \left\lceil \frac{A_{\text{total}}}{A_{\text{cell}}} \right\rceil = \left\lceil \frac{12}{2.598076 R^2} \right\rceil = \left\lceil \frac{4.6188}{R^2} \right\rceil$$

### Cluster Geometry and Reuse Distance $D$
In a regular hexagonal grid, coordinate axes are defined at $60^\circ$ separation. Moving from the center of a reference cell to a co-channel cell is achieved by walking $i$ cells along the $u$-axis, rotating $60^\circ$ counter-clockwise, and walking $j$ cells along the $v$-axis.
By the law of cosines with angle $120^\circ$ (supplementary to $60^\circ$):
$$D^2 = (i\sqrt{3}R)^2 + (j\sqrt{3}R)^2 - 2(i\sqrt{3}R)(j\sqrt{3}R)\cos(120^\circ)$$
Since $\cos(120^\circ) = -0.5$:
$$D^2 = 3R^2 (i^2 + j^2 + ij) = 3R^2 N$$
$$\therefore D = R\sqrt{3N}$$

The co-channel reuse ratio $Q$ is therefore strictly dependent on cluster size:
$$Q = \frac{D}{R} = \sqrt{3N}$$

---

## 2. Derivation of Co-Channel Signal-to-Interference Ratio (SIR)

Assuming an omnidirectional mobile at distance $r$ from its serving base station transmitting power $P_t$, received carrier power is:
$$C = P_t \cdot K_0 \cdot r^{-n}$$
where $K_0$ is a propagation constant and $n$ is the path-loss exponent.

In the worst-case downlink scenario, the mobile is located at the cell boundary: $r = R$.
Assuming $i_0$ co-channel cells in the first interfering tier, all transmitting power $P_t$, located at approximate distance $D_k \approx D$:
$$I = \sum_{k=1}^{i_0} I_k = \sum_{k=1}^{i_0} P_t \cdot K_0 \cdot D_k^{-n} \approx i_0 P_t K_0 D^{-n}$$

Taking the ratio:
$$\text{SIR} = \frac{C}{I} = \frac{P_t K_0 R^{-n}}{i_0 P_t K_0 D^{-n}} = \frac{1}{i_0} \left( \frac{D}{R} \right)^n = \frac{Q^n}{i_0} = \frac{(\sqrt{3N})^n}{i_0}$$

In decibels:
$$\text{SIR}_{\text{dB}} = 10 \log_{10}\left( \frac{(3N)^{n/2}}{i_0} \right) = 5n \log_{10}(3N) - 10 \log_{10}(i_0)$$

### Impact of Sectoring on $i_0$:
- **Omnidirectional ($360^\circ$):** Mobile receives interference from all 6 surrounding first-tier cells: $i_0 = 6$.
  $$\text{SIR}_{\text{omni}} = \frac{(3N)^{n/2}}{6}$$
- **$120^\circ$ Tri-Sectoring:** Front-to-back isolation suppresses radiation into other sectors. A mobile receives radiation from only **2 first-tier interferers**: $i_0 = 2$.
  $$\text{SIR}_{120^\circ} = \frac{(3N)^{n/2}}{2} = 3 \times \text{SIR}_{\text{omni}} \quad (+4.77\text{ dB improvement})$$
- **$60^\circ$ Six-Sectoring:** Mobile receives interference from only **1 first-tier interferer**: $i_0 = 1$.
  $$\text{SIR}_{60^\circ} = (3N)^{n/2} = 6 \times \text{SIR}_{\text{omni}} \quad (+7.78\text{ dB improvement})$$

---

## 3. Erlang-B Traffic Capacity Derivation

Let $C_c$ be the number of duplex voice channels available to a cell (or sector), $A$ be the total offered traffic in Erlangs, and $P_b$ be the probability of call blocking.
The Erlang-B loss formula is:
$$P_b = B(C_c, A) = \frac{\frac{A^{C_c}}{C_c!}}{\sum_{k=0}^{C_c} \frac{A^k}{k!}}$$

Using the stable iterative recurrence relation:
$$B(0, A) = 1$$
$$B(k, A) = \frac{A \cdot B(k-1, A)}{k + A \cdot B(k-1, A)}, \quad \text{for } k = 1, 2, \dots, C_c$$

For target blocking $P_b \le 0.02$ ($2\%$ GoS), we invert this numerically to determine supported Erlangs per cell $A_{\text{cell}}(C_c)$.
Total subscriber capacity supported across the $M$ cells:
$$U_{\text{total}} = \frac{M \cdot A_{\text{cell}}}{A_u} = \frac{M \cdot A_{\text{cell}}}{0.025}$$

---

## 4. Overall Cost–Capacity Relation

Planning and deployment cost consists of:
1. Fixed initial planning, network survey, and spectrum acquisition cost: $K_{\text{fixed}}$.
2. Per-base-station site capital expenditure (tower, civil work, transceivers, backhaul): $C_{\text{site}}$.
3. Per-sector antenna overhead: $C_{\text{sec}}$.

Total System Cost:
$$\text{Cost}_{\text{total}}(M) = K_{\text{fixed}} + M \cdot \left( C_{\text{site}} + N_{\text{sectors}} \cdot C_{\text{sec}} \right)$$

Since $M \propto 1/R^2$ and supported users $U \propto M \cdot A_{\text{cell}}$:
$$\text{Cost}(U) \approx K_1 + K_2 \cdot U$$
As cell radius $R$ decreases, infrastructure costs scale quadratically with spatial density ($O(1/R^2)$).
