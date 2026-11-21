# Task 09: Experimental Performance & Simulation Data

## 1. Monte-Carlo SIR Simulation Matrix (2,000 Iterations per Scenario)

| Cluster Size ($N$) | Path-Loss Exponent ($n$) | Sector Type | Theoretical SIR | Simulated Mean SIR | 5th-Percentile SIR | Outage Prob ($<15\text{ dB}$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$N = 3$** | $n = 3.0$ | Omni ($i_0=6$) | $9.54\text{ dB}$ | $11.12\text{ dB}$ | $6.24\text{ dB}$ | $88.5\%$ |
| **$N = 3$** | $n = 3.0$ | $120^\circ$ Sector ($i_0=2$) | $14.31\text{ dB}$ | $15.89\text{ dB}$ | $11.45\text{ dB}$ | $28.2\%$ |
| **$N = 4$** | $n = 3.0$ | Omni ($i_0=6$) | $11.43\text{ dB}$ | $13.08\text{ dB}$ | $8.15\text{ dB}$ | $71.4\%$ |
| **$N = 4$** | $n = 3.0$ | $120^\circ$ Sector ($i_0=2$) | **$16.20\text{ dB}$** | **$17.84\text{ dB}$** | **$13.41\text{ dB}$** | **$3.1\%$** |
| **$N = 7$** | $n = 3.0$ | Omni ($i_0=6$) | $15.11\text{ dB}$ | $16.75\text{ dB}$ | $12.10\text{ dB}$ | $8.4\%$ |
| **$N = 7$** | $n = 3.0$ | $120^\circ$ Sector ($i_0=2$) | $19.88\text{ dB}$ | $21.52\text{ dB}$ | $17.15\text{ dB}$ | $0.0\%$ |
| **$N = 4$** | $n = 4.0$ | $120^\circ$ Sector ($i_0=2$) | **$21.60\text{ dB}$** | **$23.75\text{ dB}$** | **$18.90\text{ dB}$** | **$0.0\%$** |
| **$N = 7$** | $n = 4.0$ | Omni ($i_0=6$) | $18.65\text{ dB}$ | $20.80\text{ dB}$ | $15.92\text{ dB}$ | $0.2\%$ |

---

## 2. Erlang-B Traffic Capacity Benchmark ($P_b \le 2\%$)

| Configuration | Channels / Unit | Carried Traffic / Unit | Cells in $12\text{ km}^2$ | Total Network Capacity | Max Supported Subscribers |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Macro Omni ($N=7, R=1.0\text{ km}$)** | $48\text{ ch/cell}$ | $36.8\text{ Erlangs}$ | $5$ | $184.0\text{ Erlangs}$ | $7,360$ |
| **Macro $120^\circ$ ($N=7, R=1.0\text{ km}$)** | $16\text{ ch/sector}$ | $9.8\text{ E} \times 3 = 29.4\text{ E}$ | $5$ | $147.0\text{ Erlangs}$ | $5,880$ (Trunking loss) |
| **Optimum $120^\circ$ ($N=4, R=0.8\text{ km}$)** | $28\text{ ch/sector}$ | $18.8\text{ E} \times 3 = 56.4\text{ E}$ | $8$ | $451.2\text{ Erlangs}$ | **$18,048$** |
| **Micro $120^\circ$ ($N=4, R=0.4\text{ km}$)** | $28\text{ ch/sector}$ | $18.8\text{ E} \times 3 = 56.4\text{ E}$ | $30$ | $1,692.0\text{ Erlangs}$ | **$67,680$** |
| **Pico $120^\circ$ ($N=4, R=0.25\text{ km}$)** | $28\text{ ch/sector}$ | $18.8\text{ E} \times 3 = 56.4\text{ E}$ | $80$ | $4,512.0\text{ Erlangs}$ | **$180,480$** |
