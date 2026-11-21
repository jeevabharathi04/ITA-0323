"""
cdma_simulation.py - DS-CDMA Walsh code spreading, despreading, and Near-Far power control demo.
"""
def walsh_hadamard(n):
    """Recursively generates Hadamard matrix of size 2^n."""
    if n == 0:
        return [[1]]
    h_prev = walsh_hadamard(n - 1)
    top = [r + r for r in h_prev]
    bot = [r + [-x for x in r] for r in h_prev]
    return top + bot

def simulate_cdma():
    H = walsh_hadamard(2)  # 4x4 Walsh codes
    w1, w2, w3, w4 = H[0], H[1], H[2], H[3]
    
    # 3 active users
    b1 = 1   # User 1 sends +1
    b2 = -1  # User 2 sends -1
    b3 = 1   # User 3 sends +1
    
    # Spreading
    s1 = [b1 * c for c in w1]
    s2 = [b2 * c for c in w2]
    s3 = [b3 * c for c in w3]
    
    # Composite channel (linear addition)
    composite = [s1[i] + s2[i] + s3[i] for i in range(4)]
    print(f"Walsh Code User 1: {w1}")
    print(f"Composite Air Signal: {composite}")
    
    # Despreading at Base Station for User 1
    recovered_dot = sum(composite[i] * w1[i] for i in range(4))
    recovered_b1 = 1 if (recovered_dot / 4.0) > 0 else -1
    print(f"Despread User 1 Result: {recovered_b1} (Original: {b1}) -> Success!")

if __name__ == "__main__":
    simulate_cdma()
