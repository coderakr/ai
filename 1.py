# Undirected Graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ---------------- DFS (Recursive) ----------------
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Visit the node
    print(node, end=" ")
    visited.add(node)

    # Recursive call for all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# ---------------- BFS ----------------
def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ---------------- Main ----------------
print("DFS Traversal:")
dfs(graph, 'A')

print("\nBFS Traversal:")
bfs(graph, 'A')