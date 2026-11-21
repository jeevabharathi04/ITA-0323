# Assignment 1 (CO1): Hexagonal Cellular Network Design & Optimization

This directory contains the engineering analysis, mathematical derivations, simulation scripts, and architectural evaluations for **CO1: Cellular Network Concepts, Frequency Reuse, Interference, and Capacity Planning**.

---

## 📑 Tasks Index

| Task Folder | Focus Area | Deliverable / Key Finding |
| :--- | :--- | :--- |
| [Task01/](Task01/explanation.md) | Frequency Planning Strategies | Formulated 3 distinct strategies (Fixed, 120° Sectoring, Dynamic Hierarchical Borrowing) with pseudocode and flowcharts. |
| [Task02/](Task02/explanation.md) | Governing Design Parameters | Identified $N, Q, R$ and traced their scaling behavior from 1,000 to 100,000+ subscribers. |
| [Task03/](Task03/derivation.md) | Mathematical Derivations | Rigorous proofs for $D = R\sqrt{3N}$, SIR formulations, Erlang-B loss model, and cost-capacity relations. |
| [Task04/](Task04/explanation.md) | Best / Average / Worst Behavior | Vertex-corner exact SIR degradation analysis and log-normal shadowing margins. |
| [Task05/](Task05/sensitivity.md) | Scaling & Sensitivity Analysis | Proportionality laws ($1/R^2, N^{n/2}$) and break-even scale transitions. |
| [Task06/](Task06/recurrence.md) | Cell Splitting Recurrence | Mathematical recurrence for cell count $M_k = 4M_{k-1}$ and power scaling $P_k = P_0 / 2^{nk}$. |
| [Task07/](Task07/solution.md) | Closed-Form Solution | Proved $k = \lceil \log_4(D_{\text{target}}/C_0) \rceil = 2$ rounds for 100k subscribers; analysed handoff growth. |
| [Task08/](Task08/cellular_planner.py) | Python Simulation Suite | Standalone Monte-Carlo hexagonal simulator and Erlang-B capacity solver. |
| [Task09/](Task09/results.md) | Simulation Results & Data | Empirical SIR CDF tables, 5th-percentile outage data, and traffic benchmarks. |
| [Task10/](Task10/comparison.md) | Theory vs Simulation | Analytical gap analysis (boundary assumptions vs spatial expectation; trunking penalties). |
| [Task11/](Task11/recommendation.md) | Final Recommendation | Defended $N=4$ ($120^\circ$ tri-sector) baseline transitioning to microcells. |
| [Task12/](Task12/stadium_challenge.md) | Day-4 Design Challenge | Solved 25,000 attendee (1,250 Erlang) stadium surge via COWs, antenna down-tilt, and Wi-Fi offload. |
