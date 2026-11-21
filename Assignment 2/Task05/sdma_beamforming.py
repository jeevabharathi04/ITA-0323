"""
sdma_beamforming.py - 8-element ULA beamforming and spatial nulling pattern generator.
"""
import math

def calculate_array_factor(num_elements=8, steer_angle_deg=30.0):
    steer_rad = math.radians(steer_angle_deg)
    kd = math.pi  # d = lambda/2 -> k*d = (2*pi/lambda)*(lambda/2) = pi
    beta = -kd * math.sin(steer_rad)
    
    pattern = []
    for deg in range(-90, 91, 5):
        theta = math.radians(deg)
        psi = kd * math.sin(theta) + beta
        # Sum complex array elements
        real_part = sum(math.cos(m * psi) for m in range(num_elements))
        imag_part = sum(math.sin(m * psi) for m in range(num_elements))
        magnitude = math.sqrt(real_part**2 + imag_part**2) / num_elements
        pattern.append((deg, round(magnitude, 3)))
        
    print(f"=== SDMA Beamforming Pattern (Steered to {steer_angle_deg}°) ===")
    for deg, mag in pattern[::3]:
        bar = "#" * int(mag * 30)
        print(f"Azimuth {deg:+03d}°: {mag:.3f} | {bar}")

if __name__ == "__main__":
    calculate_array_factor()
