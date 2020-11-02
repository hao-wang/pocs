import networkx as nx
from topological_ordering import topological_orders

if __name__ == "__main__":
    g = nx.DiGraph()
    g.add_edges_from(
        [(1, 2),
         (3, 4),
         (5, 4),
         (5, 8),
         (4, 9),
         (8, 9),
         (5, 'A'),
         ('A', 'B'),
         (2, 3),
         (2, 4),
         (6, 2),
         (2, 5),
         (7, 5),
         ('A', 'C')])

    print(topological_orders(g))
