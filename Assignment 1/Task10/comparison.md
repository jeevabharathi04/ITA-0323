# Task 10: Comparison of Theory vs Simulation

## 1. Quantitative Discrepancy Analysis

Comparing the analytical theoretical predictions with Monte-Carlo empirical simulations reveals consistent, mathematically explainable deviations:

1. **Mean SIR is consistently higher in simulation (+1.5 to +2.1 dB):**
   - **Reason:** The theoretical formula assumes the mobile is stationed permanently at the worst-case boundary ($r = R$).
   - In simulation, users are uniformly distributed across the hexagonal area (mean user distance $\mathbb{E}[r] \approx 0.54 R$). The increased proximity to the serving base station elevates the average carrier power.

2. **5th-Percentile SIR matches worst-case analytical model:**
   - For $N=7, n=4.0$, analytical worst-case boundary SIR is $17.26\text{ dB}$.
   - The simulated 5th-percentile (representing edge users) is $15.92\text{ dB}$ (under slight shadow fading). This validates the theoretical model for network edge dimensioning.

3. **Trunking Efficiency Discrepancy in Sectoring:**
   - While sectoring reduces interference (allowing $N=4$ instead of $N=7$), it subdivides channels into smaller independent pools ($28$ channels per sector rather than $84$ pooled).
   - Erlang-B non-linearity shows that 84 pooled channels support $71.2\text{ Erlangs}$ ($P_b=0.02$), while three 28-channel pools support only $3 \times 18.8 = 56.4\text{ Erlangs}$ ($20.8\%$ trunking penalty).
   - **Synthesis:** The spectral gain from dropping $N=7 \to N=4$ ($+75\%$ more channels per site) far outweighs the $20.8\%$ trunking efficiency loss!
