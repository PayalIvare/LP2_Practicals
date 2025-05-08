import heapq

# Dijkstra's algorithm function
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Function to take dynamic input from user
def dynamic_dijkstra():
    graph = {}
    try:
        n = int(input("Enter the number of nodes: "))
        print("Enter node names (e.g., A, B, C...):")
        for i in range(n):
            node = input(f"Node {i + 1}: ").strip()
            graph[node] = []

        e = int(input("Enter the number of edges: "))
        print("Enter the edges in the format 'source destination weight' (e.g., A B 4):")
        for i in range(e):
            u, v, w = input(f"Edge {i + 1}: ").split()
            w = int(w)
            if u in graph:
                graph[u].append((v, w))
            else:
                graph[u] = [(v, w)]

        start = input("Enter the starting node: ").strip()
        if start not in graph:
            print("Invalid starting node.")
            return

        distances = dijkstra(graph, start)
        print(f"Shortest paths from {start}:")
        for node, dist in distances.items():
            print(f"{start} → {node} = {dist if dist != float('inf') else '∞'}")

    except ValueError:
        print("Invalid input. Please enter numbers where required.")

# Run the function
dynamic_dijkstra()

"""
Enter the number of nodes: 4
Enter node names (e.g., A, B, C...):
Node 1: A
Node 2: B
Node 3: C
Node 4: D
Enter the number of edges: 4
Enter the edges in the format 'source destination weight' (e.g., A B 4):
Edge 1: A B 1
Edge 2: A C 4
Edge 3: B C 2
Edge 4: C D 1
Enter the starting node: A
Shortest paths from A:
A → A = 0
A → B = 1
A → C = 3
A → D = 4
"""