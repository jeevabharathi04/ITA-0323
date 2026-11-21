# Task 07 (Q7): Emergency Disaster Mobile Communication Network

## 1. Scenario: Complete Infrastructure Destruction
- In the aftermath of a major cyclone / earthquake, all cellular base stations and fiber backhauls in the township are destroyed.
- First responders, ambulances, and search-and-rescue teams require continuous voice and spatial coordination.

---

## 2. Resilient Hybrid Mesh Network Blueprint
```text
Disaster Response Tactical Network:
  ├── Tier 1: Incident Command Post (Satellite Starlink Backhaul)
  │     └── Transportable LEO Satellite Terminal connecting to national emergency dispatch.
  │
  ├── Tier 2: Vehicle-Mounted Tactical Mesh Routers (AODV over 5.8 GHz ISM)
  │     └── Ambulances and police vehicles form a mobile backbone mesh covering 12 km².
  │     └── AODV reactive routing adapts dynamically as vehicles navigate damaged streets.
  │
  ├── Tier 3: Portable Wi-Fi 6 / Bluetooth Low Energy (BLE) Rescue Beacons
  │     └── Wearable tactical radios for ground rescue teams.
  │     └── Duty-cycled sleep modes extend battery life to 72 hours.
```
