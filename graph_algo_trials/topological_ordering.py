def topological_orders(network):
    """
    Suppose we know the root elements:

        Breadth first search
    :return:
        Topologically sorted array
    """
    nodes = network.nodes()
    visited = {}
    ordered = []
    for ind, node in enumerate(nodes):
        if node in visited:
            continue

        ordered.insert(0, node)
        visited[node] = 1
        parents = network.predecessors(node)
        for p in parents:
            if p in visited:
                continue

            visited[p] = 1
            ordered.insert(0, p)

    return ordered


