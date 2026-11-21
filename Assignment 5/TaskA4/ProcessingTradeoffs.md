# Task A4: Local vs Cloud vs Hybrid Computation Offloading

## 1. Mathematical Energy Trade-Off Model

Let:
- $E_{\text{local}}$ be the energy consumed executing task on the mobile device:
  $$E_{\text{local}} = P_{\text{CPU}} \cdot T_{\text{exec}} = P_{\text{CPU}} \cdot \frac{W}{f_{\text{CPU}}}$$
  where $W$ is computational cycles required, and $P_{\text{CPU}}$ is processor power.
- $E_{\text{cloud}}$ be the energy consumed offloading task over cellular radio:
  $$E_{\text{cloud}} = P_{\text{tx}} \cdot \left( \frac{D_{\text{in}}}{R_{\text{uplink}}} \right) + P_{\text{idle}} \cdot T_{\text{server}} + P_{\text{rx}} \cdot \left( \frac{D_{\text{out}}}{R_{\text{downlink}}} \right)$$

### Offloading Decision Rule:
Offload to cloud if and only if:
$$E_{\text{cloud}} < E_{\text{local}} \quad \text{and} \quad T_{\text{total,cloud}} < T_{\text{deadline}}$$

**Practical Implications:**
- **High-Data, Low-Compute (e.g., Simple Image Filtering):** Process locally ($E_{\text{local}} \ll E_{\text{cloud}}$).
- **Low-Data, High-Compute (e.g., Deep Learning Model Inference):** Offload to cloud ($E_{\text{cloud}} \ll E_{\text{local}}$).
