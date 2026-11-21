"""
ofdma_scheduler.py - Channel-aware opportunistic subcarrier scheduler demo.
"""
import random

def ofdma_scheduling_demo(num_users=4, num_subcarriers=12):
    random.seed(42)
    # Generate random SNR matrix (users x subcarriers)
    snr_matrix = [[random.uniform(5.0, 30.0) for _ in range(num_subcarriers)] for _ in range(num_users)]
    
    allocation = {}
    total_capacity = 0.0
    
    for sc in range(num_subcarriers):
        best_user = max(range(num_users), key=lambda u: snr_matrix[u][sc])
        best_snr = snr_matrix[best_user][sc]
        # Shannon capacity: B * log2(1 + SNR)
        cap = 15.0 * math.log2(1.0 + 10.0 ** (best_snr / 10.0))  # 15 kHz subcarrier
        allocation[sc] = (best_user, round(best_snr, 1), round(cap, 1))
        total_capacity += cap
        
    print("=== OFDMA Subcarrier Allocation Map ===")
    for sc, (u, snr, cap) in allocation.items():
        print(f"Subcarrier {sc:02d} -> User {u} (SNR: {snr} dB, Capacity: {cap} kbps)")
    print(f"Total Aggregated Multi-User Capacity: {total_capacity/1000.0:.2f} Mbps")

if __name__ == "__main__":
    import math
    ofdma_scheduling_demo()
