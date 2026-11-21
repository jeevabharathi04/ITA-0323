# Task A5: Heuristic & Approximate Optimization for Mobile Energy

When battery state drops below $20\%$, exact optimization must gracefully degrade to approximate heuristics:
1. **Dynamic GPS Throttling:** Switch from high-accuracy GPS ($100\text{ mA}$) to cell-tower triangulation or pedometer step-counting ($2\text{ mA}$), trading $50\text{ m}$ accuracy for $50\times$ battery conservation.
2. **Image Downsampling:** Compress image uploads to $70\%$ JPEG before transmission, reducing radio transmitter on-time by $4\times$.
3. **Batch Network Dispatches:** Defer non-critical sensor uploads until device connects to AC charging or Wi-Fi.
