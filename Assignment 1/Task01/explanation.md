# Task 01: Design Alternative Frequency-Planning Strategies

## 1. Problem Context & Planning Constraints
- **Township Area:** $A_{\text{total}} = 12\text{ km}^2$
- **Total Channel Allocation:** $S = 336$ duplex voice channels (after deducting control/signaling channels).
- **Target Subscriber Scale:** $1,000 \to 10,000 \to 20,000 \to 100,000+$ users.
- **Traffic Profile:** Busy-hour traffic $A_u = 0.025\text{ Erlang/user}$; Grade of Service (GoS) $\le 2\%$ blocking ($P_b \le 0.02$).
- **Co-Channel Interference Threshold:** Minimum required Signal-to-Interference Ratio $\text{SIR}_{\text{min}} = 15\text{ dB}$ (digital threshold balancing modulation requirements and spectral efficiency).
- **Path-Loss Exponent:** $n = 3.0$ (suburban/campus mixed terrain) to $n = 4.0$ (dense academic block clusters).

---

## 2. Three Distinct Frequency-Planning Strategies

### Strategy A: Fixed Cluster Reuse with Hexagonal Tiling (Baseline Iterative Scheme)
- **Core Principle:** Spatial reuse based on regular geometric tessellation ($N = i^2 + ij + j^2$).
- **Mechanism:**
  1. The 336 channels are partitioned equally into $N$ disjoint channel subsets: $K = \lfloor S / N \rfloor$.
  2. The cluster pattern is replicated periodically across the 2D plane.
  3. Co-channel cells are separated by the reuse distance $D = R\sqrt{3N}$, maintaining a constant reuse ratio $Q = D/R = \sqrt{3N}$.
- **Access Channel Sharing:** 
  - Control channels (BCCH/CCCH) are assigned dedicated frequencies from each subset to prevent signaling collision.
  - Traffic channels (TCH) operate under FDMA/TDMA frames (e.g., GSM-style 8 time-slots per carrier).
- **Algorithmic Nature:** Iterative grid search over admissible integers $(i, j)$ to find the minimum $N$ satisfying $\text{SIR} \ge 15\text{ dB}$.

#### Pseudocode (Iterative Grid Allocation):
```text
Algorithm FixedClusterAllocation(TotalChannels S, RequiredSIR sir_target, PathLossExponent n):
    AdmissibleClusters = [3, 4, 7, 9, 12, 13, 19, 21]
    SelectedCluster = None
    
    For N in AdmissibleClusters:
        Q = sqrt(3 * N)
        // Worst-case 1st-tier omnidirectional co-channel interference (6 interferers)
        SIR_approx = 10 * log10((Q^n) / 6)
        If SIR_approx >= sir_target:
            SelectedCluster = N
            Break
            
    ChannelsPerCell = floor(S / SelectedCluster)
    Partition S into SelectedCluster disjoint sets {C_1, C_2, ..., C_N}
    
    For each cell (u, v) in HexagonalGrid:
        ClusterIndex = (u * i + v * j) mod SelectedCluster
        AssignChannels(cell=(u, v), channel_set=C_ClusterIndex)
        
    Return GridAssignment, ChannelsPerCell
```

---

### Strategy B: Micro-Sectorized Reuse (120° / 60° Directional Spatial Filtering)
- **Core Principle:** Directional spatial filtering at the base station to suppress co-channel interferers.
- **Mechanism:**
  - Base station antennas are replaced by directional sector antennas ($120^\circ$ tri-sector or $60^\circ$ six-sector).
  - In a $120^\circ$ 3-sector cell, each cell is split into 3 distinct sectors, each allocated $K/3$ channels.
  - Crucially, a mobile station in any sector only receives co-channel interference from **2 first-tier interferers** instead of 6 in omnidirectional cells:
    $$\text{SIR}_{120^\circ} \approx \frac{(\sqrt{3N})^n}{2}$$
  - This allows operating at a tighter cluster size (e.g., $N=4$ or $N=3$) while still meeting $\text{SIR} \ge 15\text{ dB}$, dramatically boosting system capacity.
- **Access Channel Sharing:** Each sector carries its own broadcast control channel (BCCH) and independent traffic channel pools.

#### Pseudocode (Sectorized Planning):
```text
Algorithm SectorizedPlanning(TotalChannels S, TargetCapacity Users, TargetGoS 0.02):
    N = 4 // Tighter cluster enabled by sectoring
    NumSectorsPerCell = 3
    ChannelsPerSector = floor(S / (N * NumSectorsPerCell)) // 336 / (4 * 3) = 28 channels/sector
    
    ErlangPerSector = ErlangB_Solve(Channels=ChannelsPerSector, Blocking=0.02)
    TotalCellCapacityErlang = NumSectorsPerCell * ErlangPerSector
    
    For cell in Grid:
        OrientAntennas(cell, angles=[0, 120, 240])
        For sector in [0, 1, 2]:
            AssignFrequencies(cell, sector, SetIndex=(cell.cluster_id * 3 + sector))
            
    Return SectorLayout
```

---

### Strategy C: Dynamic Channel Borrowing with Hierarchical Underlay/Overlay (Recursive Splitting)
- **Core Principle:** Non-uniform traffic adaptation and recursive spatial scaling.
- **Mechanism:**
  - Standard macrocells provide continuous baseline coverage.
  - When traffic density in hotspot zones (academic centers, libraries) exceeds threshold capacity, overloaded cells are recursively split ($R \to R/2$).
  - Dynamic channel borrowing algorithm allows borrowing channels from nominal co-channel neighbors under strict channel-locking constraints (channels borrowed in cell $A$ are locked in co-channel cells within distance $D$ to prevent co-channel interference).
- **Algorithmic Nature:** Recursive quad-tree spatial splitting with dynamic priority queue reallocation.

#### Pseudocode (Recursive Hotspot Splitting & Borrowing):
```text
Algorithm RecursiveCellSplit(Cell C, Demand D_current, Capacity C_max):
    If D_current <= C_max:
        Return [C] // Stable cell
    Else:
        // Split cell of radius R into 4 sub-cells of radius R/2
        SubCells = GenerateSubHexagons(Center=C.center, Radius=C.radius / 2, Count=4)
        P_tx_new = C.transmit_power / (2^PathLossExponent)
        
        ResultSet = []
        For sub in SubCells:
            sub.power = P_tx_new
            sub.demand = EstimateLocalDemand(sub.area)
            sub.nominal_channels = AllocateUnderlaySpectrum(sub)
            ResultSet.extend(RecursiveCellSplit(sub, sub.demand, Capacity(sub.nominal_channels)))
            
        Return ResultSet
```

---

## 3. Comparison of Planning Strategies

| Parameter | Strategy A: Fixed Cluster | Strategy B: 120° Sectoring | Strategy C: Hierarchical / Borrowing |
| :--- | :--- | :--- | :--- |
| **Design Principle** | Spatial Tessellation Reuse | Directional Spatial Filtering | Adaptive Spatial Scaling & Borrowing |
| **Cluster Size ($N$)** | $N = 7$ (Omni) | $N = 4$ ($120^\circ$ sectors) | Hybrid Macro ($N=7$) / Micro ($N=3$) |
| **Channels / Cell** | $48$ | $84$ (28 per sector $\times 3$) | Dynamic (Nominal: 48, Peak: 72+) |
| **1st-Tier Interferers ($i_0$)** | $6$ | $2$ | $1$ to $3$ (directional/micro) |
| **Trunking Efficiency** | Highest per cell pool | Moderate (split into 3 pools) | High (dynamic channel pooling) |
| **Handoff Complexity** | Low (inter-cell only) | Medium (inter-sector soft/hard) | High (macro-micro vertical handoffs) |
| **Preprocessing Overhead** | Low (basic survey & grid) | Medium (antenna pattern engineering) | High (continuous traffic monitoring & locking) |
