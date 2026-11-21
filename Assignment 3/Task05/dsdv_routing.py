"""
dsdv_routing.py - DSDV routing table convergence and loop-free sequence update simulator.
"""
class DSDVNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.sequence_number = 0
        self.table = {}  # dest -> (next_hop, metric, seq_num)
        # Self-entry
        self.table[node_id] = (node_id, 0, self.sequence_number)

    def increment_seq(self):
        self.sequence_number += 2
        self.table[self.node_id] = (self.node_id, 0, self.sequence_number)

    def receive_update(self, neighbor_id, updates):
        updated = False
        for dest, (metric, seq_num) in updates.items():
            new_metric = metric + 1
            if dest not in self.table:
                self.table[dest] = (neighbor_id, new_metric, seq_num)
                updated = True
            else:
                curr_hop, curr_metric, curr_seq = self.table[dest]
                if seq_num > curr_seq:
                    self.table[dest] = (neighbor_id, new_metric, seq_num)
                    updated = True
                elif seq_num == curr_seq and new_metric < curr_metric:
                    self.table[dest] = (neighbor_id, new_metric, seq_num)
                    updated = True
        return updated

if __name__ == "__main__":
    A, B, C = DSDVNode("A"), DSDVNode("B"), DSDVNode("C")
    # Linear topology: A <-> B <-> C
    B.receive_update("A", {"A": (0, A.sequence_number)})
    B.receive_update("C", {"C": (0, C.sequence_number)})
    A.receive_update("B", {"B": (0, 0), "C": (1, C.sequence_number)})
    
    print("=== DSDV Routing Table at Node A ===")
    for dest, (nxt, cost, seq) in A.table.items():
        print(f"Dest: {dest} | NextHop: {nxt} | Cost: {cost} hops | SeqNum: {seq}")
