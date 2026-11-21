"""
cellular_planner.py - Hexagonal Cellular Network Planning & Monte-Carlo SIR Simulation Tool
Author: PRADEEPRAMM05
Course: ITA0323 - Mobile Computing
"""

import math
import random

class CellularPlanner:
    def __init__(self, total_area_km2=12.0, total_channels=336, target_gos=0.02):
        self.total_area = total_area_km2
        self.total_channels = total_channels
        self.target_gos = target_gos

    @staticmethod
    def erlang_b(channels, offered_traffic_erlang):
        """Iterative computation of Erlang-B loss probability."""
        if channels == 0:
            return 1.0
        b = 1.0
        for k in range(1, channels + 1):
            b = (offered_traffic_erlang * b) / (k + offered_traffic_erlang * b)
        return b

    def find_max_capacity_erlang(self, channels, target_blocking=0.02, tolerance=1e-3):
        """Bisection search to find max carried Erlangs for given channels and GoS."""
        if channels <= 0:
            return 0.0
        low = 0.0
        high = channels * 2.0
        for _ in range(50):
            mid = (low + high) / 2.0
            pb = self.erlang_b(channels, mid)
            if abs(pb - target_blocking) < tolerance:
                return mid
            elif pb < target_blocking:
                low = mid
            else:
                high = mid
        return (low + high) / 2.0

    @staticmethod
    def hexagonal_cell_area(radius_km):
        return (3.0 * math.sqrt(3.0) / 2.0) * (radius_km ** 2)

    def calculate_cell_count(self, radius_km):
        cell_area = self.hexagonal_cell_area(radius_km)
        return math.ceil(self.total_area / cell_area)

    @staticmethod
    def theoretical_sir(cluster_size, path_loss_exponent, num_interferers=6):
        reuse_ratio = math.sqrt(3.0 * cluster_size)
        sir_linear = (reuse_ratio ** path_loss_exponent) / float(num_interferers)
        sir_db = 10.0 * math.log10(sir_linear)
        return sir_linear, sir_db

    def monte_carlo_sir_simulation(self, cluster_size, path_loss_exp, radius_km, 
                                   num_samples=10000, sector_type='omni', shadow_sigma_db=0.0):
        """
        Simulates downlink SIR distribution across a hexagonal cell grid.
        Generates random user locations and calculates exact path loss from serving
        and 1st-tier co-channel interferers.
        """
        D = radius_km * math.sqrt(3.0 * cluster_size)
        
        # 1st-tier interferer angles
        if sector_type == 'omni':
            num_interferers = 6
            interferer_angles = [i * (math.pi / 3.0) for i in range(6)]
        elif sector_type == '120_sector':
            num_interferers = 2
            interferer_angles = [math.pi / 6.0, 5.0 * math.pi / 6.0]
        elif sector_type == '60_sector':
            num_interferers = 1
            interferer_angles = [math.pi / 2.0]
        else:
            raise ValueError("Unknown sector type")

        sir_samples_db = []
        
        for _ in range(num_samples):
            # Sample random mobile inside serving hexagon (rejection sampling)
            while True:
                rx = (random.random() * 2.0 - 1.0) * radius_km
                ry = (random.random() * 2.0 - 1.0) * radius_km
                d_sq = rx * rx + ry * ry
                if d_sq > radius_km * radius_km:
                    continue
                # Hexagon boundary constraint: sqrt(3)*|x| + |y| <= sqrt(3)*R
                if math.sqrt(3.0) * abs(rx) + abs(ry) <= math.sqrt(3.0) * radius_km:
                    d_serving = max(math.sqrt(d_sq), 0.01 * radius_km)
                    break
            
            # Serving Carrier Power
            serving_power = (d_serving) ** (-path_loss_exp)
            if shadow_sigma_db > 0.0:
                shadow = random.gauss(0.0, shadow_sigma_db)
                serving_power *= 10.0 ** (shadow / 10.0)

            # Summed Co-Channel Interferers
            interference_sum = 0.0
            for angle in interferer_angles:
                bs_x = D * math.cos(angle)
                bs_y = D * math.sin(angle)
                dist_interf = math.sqrt((rx - bs_x) ** 2 + (ry - bs_y) ** 2)
                interf_pwr = (dist_interf) ** (-path_loss_exp)
                if shadow_sigma_db > 0.0:
                    sh_int = random.gauss(0.0, shadow_sigma_db)
                    interf_pwr *= 10.0 ** (sh_int / 10.0)
                interference_sum += interf_pwr

            sir_lin = serving_power / max(interference_sum, 1e-15)
            sir_db = 10.0 * math.log10(sir_lin)
            sir_samples_db.append(sir_db)

        sir_samples_db.sort()
        mean_sir = sum(sir_samples_db) / len(sir_samples_db)
        p5_sir = sir_samples_db[int(0.05 * len(sir_samples_db))]
        p50_sir = sir_samples_db[int(0.50 * len(sir_samples_db))]
        outage_prob = sum(1 for s in sir_samples_db if s < 15.0) / float(len(sir_samples_db))

        return {
            "cluster_size": cluster_size,
            "path_loss_exp": path_loss_exp,
            "sector_type": sector_type,
            "mean_sir_db": round(mean_sir, 2),
            "p50_sir_db": round(p50_sir, 2),
            "p5_sir_db": round(p5_sir, 2),
            "outage_prob": round(outage_prob, 4)
        }

if __name__ == "__main__":
    planner = CellularPlanner(total_area_km2=12.0, total_channels=336)
    print("=== Cellular Network Planner Verification ===")
    for N in [3, 4, 7, 12]:
        for n in [2.5, 3.0, 4.0]:
            omni_res = planner.monte_carlo_sir_simulation(N, n, radius_km=0.8, num_samples=2000, sector_type='omni')
            sec_res = planner.monte_carlo_sir_simulation(N, n, radius_km=0.8, num_samples=2000, sector_type='120_sector')
            print(f"N={N}, n={n} | Omni Mean SIR: {omni_res['mean_sir_db']} dB (Outage: {omni_res['outage_prob']*100:.1f}%) | 120° Sector Mean SIR: {sec_res['mean_sir_db']} dB (Outage: {sec_res['outage_prob']*100:.1f}%)")
