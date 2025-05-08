def kruskal(nodes, edges):
    parent = {i: i for i in nodes}

    def find(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n

    def union(u, v):
        root1, root2 = find(u), find(v)
        if root1 != root2:
            parent[root2] = root1
            return True
        return False

    mst_weight = 0
    mst_edges = []
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_edges, mst_weight

# Function to take dynamic input
def dynamic_kruskal():
    # Input number of nodes and edges
    try:
        n = int(input("Enter the number of nodes: "))
        nodes = []
        print("Enter the nodes (e.g., A, B, C, ...):")
        for i in range(n):
            node = input(f"Node {i + 1}: ")
            nodes.append(node)

        e = int(input("Enter the number of edges: "))
        edges = []

        print("Enter the edges in the format 'node1 node2 weight' (e.g., A B 3):")
        for i in range(e):
            u, v, weight = input(f"Edge {i + 1}: ").split()
            weight = int(weight)
            edges.append((u, v, weight))

        # Call Kruskal's algorithm with dynamic nodes and edges
        mst, cost = kruskal(nodes, edges)
        print("Edges in MST (Kruskal):", mst)
        print("Total cost:", cost)

    except ValueError:
        print("Invalid input. Please enter valid integers for weights.")

# Call the dynamic Kruskal function
dynamic_kruskal()

"""

Enter the number of nodes: 4
Enter the nodes (e.g., A, B, C, ...):
Node 1: A
Node 2: B
Node 3: C
Node 4: D
Enter the number of edges: 5
Enter the edges in the format 'node1 node2 weight' (e.g., A B 3):
Edge 1: A B 1
Edge 2: B C 1
Edge 3: A C 3
Edge 4: C D 5
Edge 5: B D 6
Edges in MST (Kruskal): [('A', 'B', 1), ('B', 'C', 1), ('C', 'D', 5)]
Total cost: 7

"""