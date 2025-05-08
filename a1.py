# Create an empty graph
graph = {}

# Add edge to the graph (undirected)
def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# Recursive DFS
def dfs(node, visited):
    visited.append(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# BFS using a queue (list)
def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Main part
edges = int(input("How many edges? "))
print("Enter edges like A B:")
for i in range(edges):
    u, v = input().split()
    add_edge(u, v)

start = input("Start node: ")

print("\nDFS:")
dfs(start, [])

print("\n\nBFS:")
bfs(start)

""""
Enter the number of edges: 5
Enter each edge in the format 'A B':
A B
A C
B D
C E
E F

Enter the start node: A

Depth First Search (DFS):
A B D C E F

Breadth First Search (BFS):
A B C D E F
"""
