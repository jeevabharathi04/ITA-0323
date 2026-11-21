# Task 06 (Q6): Reactive Routing — AODV vs DSR

## 1. On-Demand Route Discovery Mechanism
Unlike proactive protocols (which continuously maintain tables for all nodes), reactive protocols discover routes only when a packet needs to be transmitted.

### A. Ad-Hoc On-Demand Distance Vector (AODV):
- **Route Request (RREQ):** Source broadcasts RREQ. Intermediate nodes create reverse-path pointers back to the source.
- **Route Reply (RREP):** Destination (or intermediate node with fresh route) unicasts RREP back along the reverse path, setting up forward-path pointers.
- **Table-Driven Hop-by-Hop:** Routing decisions are made locally at each node based on destination sequence numbers.

### B. Dynamic Source Routing (DSR):
- **Source Routing:** The entire sequence of intermediate nodes `[Source, Node1, Node2, ..., Dest]` is carried directly in the packet header.
- Intermediate nodes do not maintain routing tables; they simply inspect the header and forward to the next listed address.
- **Trade-off:** DSR avoids routing table state at intermediate nodes, but imposes massive packet header overhead as path length increases.
