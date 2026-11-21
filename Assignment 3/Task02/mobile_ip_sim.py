"""
mobile_ip_sim.py - Latency and overhead simulation of Triangular Routing vs Route Optimization.
"""
def evaluate_mobile_ip_latency(cn_to_ha_ms=65, ha_to_fa_ms=75, cn_to_fa_direct_ms=25):
    triangular_latency = cn_to_ha_ms + ha_to_fa_ms
    optimized_latency = cn_to_fa_direct_ms
    
    encapsulation_overhead_bytes = 20  # IP-in-IP tunnel header
    
    print(f"=== Mobile IP Routing Latency Analysis ===")
    print(f"Standard Triangular Routing Delay: {triangular_latency} ms")
    print(f"Route-Optimized Direct Path Delay: {optimized_latency} ms")
    print(f"Latency Improvement: {triangular_latency - optimized_latency} ms ({((triangular_latency - optimized_latency)/triangular_latency)*100:.1f}% reduction)")
    print(f"IP-in-IP Header Overhead per packet: {encapsulation_overhead_bytes} bytes")

if __name__ == "__main__":
    evaluate_mobile_ip_latency()
