"""
manet_routing_sim.py - Reactive route discovery simulation (AODV RREQ/RREP flooding).
"""
class MANETSimulator:
    def __init__(self, adjacency_list):
        self.adj = adjacency_list

    def aodv_route_discovery(self, source, destination):
        visited = {source: None}
        queue = [source]
        broadcast_count = 0
        
        while queue:
            curr = queue.pop(0)
            if curr == destination:
                break
            broadcast_count += 1
            for neighbor in self.adj.get(curr, []):
                if neighbor not in visited:
                    visited[neighbor] = curr
                    queue.append(neighbor)
                    
        # Trace path back
        if destination not in visited:
            return None, broadcast_count
        path = []
        curr = destination
        while curr is not None:
            path.append(curr)
            curr = visited[curr]
        path.reverse()
        return path, broadcast_count

if __name__ == "__main__":
    # Mesh topology: S -> A/B -> C -> D
    topology = {
        "S": ["A", "B"],
        "A": ["S", "C"],
        "B": ["S", "C"],
        "C": ["A", "B", "D"],
        "D": ["C"]
    }
    sim = MANETSimulator(topology)
    path, overhead = sim.aodv_route_discovery("S", "D")
    print(f"Discovered Path: {' -> '.join(path)} (RREQ Broadcast Overhead: {overhead} transmissions)")
