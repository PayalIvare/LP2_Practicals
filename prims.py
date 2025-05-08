import heapq

# Prim's algorithm implementation
def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # Start with the initial node with a cost of 0
    mst_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    return mst_cost

# Dynamic function to input the graph
def dynamic_prim():
    try:
        # Input number of vertices (nodes)
        n = int(input("Enter the number of vertices: "))
        
        graph = {}

        # Input each edge with its weight
        print("Enter the edges in the format: Vertex1 Vertex2 Weight")
        for _ in range(int(input("Enter the number of edges: "))):
            u, v, w = input("Enter edge (u v weight): ").split()
            w = int(w)
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            # Adding undirected edges
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Input the starting vertex for Prim's algorithm
        start = input("Enter the starting vertex: ")

        # Calculate the total cost of the MST
        mst_cost = prim(graph, start)
        print(f"Total cost of MST (Prim): {mst_cost}")

    except ValueError:
        print("Invalid input. Please enter valid integers for weights and valid vertex names.")

# Call the dynamic function
dynamic_prim()


"""
Enter the number of vertices: 4
Enter the number of edges: 5
Enter edge (u v weight): A B 1
Enter edge (u v weight): A C 3
Enter edge (u v weight): B C 1
Enter edge (u v weight): B D 6
Enter edge (u v weight): C D 5
Enter the starting vertex: A
Total cost of MST (Prim): 7
"""