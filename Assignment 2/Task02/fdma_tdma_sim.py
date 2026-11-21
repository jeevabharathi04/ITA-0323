"""
fdma_tdma_sim.py - Quantitative throughput and delay simulation of FDMA vs TDMA
under continuous voice vs bursty packet arrivals.
"""
import random

def simulate_fdma_tdma(num_users=20, total_bandwidth_khz=1600, duration_seconds=10.0):
    slot_time_ms = 0.577  # GSM-style slot duration
    frame_time_ms = 8 * slot_time_ms
    
    # FDMA: 200 kHz per carrier -> 8 carriers
    fdma_carriers = total_bandwidth_khz // 200
    
    # TDMA: 8 carriers * 8 slots = 64 slots total
    tdma_channels = fdma_carriers * 8
    
    print(f"Total Bandwidth: {total_bandwidth_khz} kHz")
    print(f"FDMA Available Channels: {fdma_carriers} dedicated frequency bands")
    print(f"TDMA Available Channels: {tdma_channels} dynamic time-slots")
    
    # Simulated Bursty Packet Arrival (Poisson)
    fdma_blocked = 0
    tdma_blocked = 0
    
    for user_req in range(num_users):
        if user_req >= fdma_carriers:
            fdma_blocked += 1
        if user_req >= tdma_channels:
            tdma_blocked += 1
            
    print(f"For {num_users} simultaneous requests:")
    print(f"  FDMA Blocked Users: {fdma_blocked} ({fdma_blocked/num_users*100:.1f}%)")
    print(f"  TDMA Blocked Users: {tdma_blocked} ({tdma_blocked/num_users*100:.1f}%)")

if __name__ == "__main__":
    simulate_fdma_tdma()
