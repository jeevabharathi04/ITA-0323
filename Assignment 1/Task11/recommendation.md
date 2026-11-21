# Task 11: Final Design Recommendation & Defence

## 1. Recommended Deployment Blueprint for University Township

- **Architecture:** 3-Tier Hierarchical Heterogeneous Network (HetNet).
- **Macrocell Baseline:**
  - **Cluster Size:** $N = 4$
  - **Antenna Layout:** $120^\circ$ Tri-Sector Directional Antennas
  - **Channels per Sector:** $28\text{ channels}$ ($84\text{ channels/site}$)
  - **Initial Cell Radius:** $R_0 = 0.8\text{ km}$ ($M_0 = 8\text{ Base Stations}$ covering $12\text{ km}^2$)
  - **Downlink Transmit Power:** $P_{\text{tx}} = 20\text{ W}$ ($43\text{ dBm}$)
  - **Expected Performance:** Mean $\text{SIR} = 17.84\text{ dB}$ ($> 15\text{ dB}$ target); Outage $< 3.2\%$.
  - **Baseline Capacity:** $8 \times 56.4\text{ E} = 451.2\text{ Erlangs} \implies 18,048\text{ active subscribers}$.

- **Evolution Roadmap:**
  - **At 20,000 to 50,000 Users:** Selectively split 4 central cells (academic area & hostels) to $R = 0.4\text{ km}$. Power scaled to $P_{\text{tx}} = 2.5\text{ W}$.
  - **At 100,000+ Users:** Complete secondary split to $R = 0.25\text{ km}$ ($M = 80\text{ microcells}$), delivering $4,512\text{ Erlangs}$ capacity ($180,480$ subscribers).
