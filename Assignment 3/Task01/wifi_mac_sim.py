"""
wifi_mac_sim.py - Monte-Carlo simulation of CSMA/CA backoff with and without RTS/CTS
under the Hidden Terminal scenario.
"""
import random

def simulate_csma_ca(num_trials=5000, enable_rts_cts=False):
    collisions = 0
    success = 0
    
    for _ in range(num_trials):
        # Hidden nodes A and C independently decide to transmit in a time window
        tx_A = random.random() < 0.35
        tx_C = random.random() < 0.35
        
        if tx_A and tx_C:
            if not enable_rts_cts:
                # Direct collision of large data packets
                collisions += 1
            else:
                # RTS collision is detected quickly; CTS grants clear channel
                if random.random() < 0.5:
                    success += 1
                else:
                    collisions += 1
        elif tx_A or tx_C:
            success += 1
            
    total = success + collisions
    print(f"RTS/CTS Enabled: {enable_rts_cts}")
    print(f"  Total Packets: {total}")
    print(f"  Successful Transmissions: {success} ({success/total*100:.1f}%)")
    print(f"  Collisions: {collisions} ({collisions/total*100:.1f}%)")

if __name__ == "__main__":
    print("=== 802.11 MAC Collision Simulation ===")
    simulate_csma_ca(enable_rts_cts=False)
    simulate_csma_ca(enable_rts_cts=True)
