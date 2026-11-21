# Task 02: Governing Design Parameters

## 1. Identification of Governing Parameters

In cellular network engineering, three fundamental parameters govern capacity, coverage, and interference:

1. **Cluster Size ($N$):**
   - The number of cells that collectively utilize the entire allocated spectrum ($S = 336$ channels).
   - Constrained geometrically to values given by the tessellation equation:
     $$N = i^2 + ij + j^2, \quad i, j \in \mathbb{Z}_{\ge 0}$$
     Allowable values: $N \in \{1, 3, 4, 7, 9, 12, 13, 19, 21, \dots\}$.
   - **Direct Impact:** 
     - Channels per cell: $K = S / N$. Decreasing $N$ directly increases spectrum allocated per cell.
     - Co-channel Reuse Ratio: $Q = D/R = \sqrt{3N}$. Decreasing $N$ brings co-channel cells closer, increasing interference.

2. **Co-Channel Reuse Ratio ($Q = D/R$):**
   - Purely dimensionless ratio of distance between co-channel cell centers ($D$) to cell radius ($R$).
   - Governs the carrier-to-interference ratio (SIR) independently of the physical scale:
     $$\text{SIR} \approx \frac{Q^n}{i_0} = \frac{(\sqrt{3N})^n}{i_0}$$
     where $i_0$ is the number of co-channel interferers in the first tier.

3. **Cell Radius ($R$):**
   - Defines the physical coverage area of each hexagonal cell:
     $$A_{\text{cell}} = \frac{3\sqrt{3}}{2} R^2 \approx 2.598 R^2$$
   - Governs the total number of cells ($M$) required to cover the $12\text{ km}^2$ township:
     $$M = \left\lceil \frac{A_{\text{total}}}{A_{\text{cell}}} \right\rceil = \left\lceil \frac{12}{2.598 R^2} \right\rceil$$
   - Controls **spatial capacity density** (Erlangs/km²).

---

## 2. Dynamic Trajectory as Subscribers Grow (1,000 to 100,000+)

As the township population expands across the planning horizon, the governing parameters must adapt across three distinct operational regimes:

```text
Phase 1: 1,000 Users (Coverage-Limited Regime)
  └── Total Demand: 1,000 × 0.025 = 25 Erlangs.
  └── Action: Large cell radius R ≈ 1.25 km (M ≈ 3 cells cover 12 km²).
  └── Cluster size N = 7 (Omni); channels per cell K = 48.
  └── Capacity is far higher than demand; system is bounded purely by propagation coverage.

Phase 2: 10,000 to 20,000 Users (Interference-Limited Regime)
  └── Total Demand: 250 to 500 Erlangs.
  └── Action: Maintain R ≈ 0.8 km; Introduce 120° Sectoring (Strategy B).
  └── Shift from N = 7 (Omni) to N = 4 (Sectored); i_0 drops from 6 to 2.
  └── Channels per cell rise to 84 (28 per sector); provides ~60 Erlangs/cell.

Phase 3: 100,000+ Users (Density & Cell-Splitting Regime)
  └── Total Demand: 100,000 × 0.025 = 2,500 Erlangs.
  └── Action: Cluster size N cannot shrink below 3; R must be aggressively scaled down.
  └── Recursive cell splitting: R drops from 0.8 km to 0.4 km, then 0.2 km (microcells).
  └── Total cells M increases from ~15 to ~240 sites.
  └── Transmit power scaled down: P_tx' = P_tx / 2^n to maintain identical boundary interference.
```
