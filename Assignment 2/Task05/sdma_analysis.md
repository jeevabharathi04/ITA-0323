# Task 05 (Q5): Space Division Multiple Access (SDMA) & Smart Antennas

## 1. Principles of SDMA & Beamforming
- Uses multi-element phased antenna arrays at the base station.
- Controls the relative phase $\Delta \phi$ and amplitude across array elements to steer high-gain narrow radiation beams directly toward desired users while synthesizing deep **nulls** toward co-channel interferers.
- Reuses the identical frequency and time slot simultaneously within the same cell for geographically separated users.

---

## 2. Mathematical Array Factor Formulation
For a Uniform Linear Array (ULA) of $M$ isotropic elements separated by distance $d = \lambda/2$:
$$\text{AF}(\theta) = \sum_{m=0}^{M-1} w_m e^{j m k d \sin \theta} = \sum_{m=0}^{M-1} a_m e^{j m (k d \sin \theta + \beta)}$$
where $\beta$ is the progressive phase shift applied to steer the main beam to target azimuth $\theta_0$:
$$\beta = -k d \sin \theta_0 = -\pi \sin \theta_0$$
