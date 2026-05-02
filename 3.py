# Implement Greedy search algorithm for Minimum Spanning Tree

import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0

    print("Edges in MST:")

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        print(f"Visited {node} with cost {weight}")

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost, neighbor))

    print("Total Cost of MST:", total_cost)


# ---------------- Graph ----------------
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}

# ---------------- Main ----------------
prims(graph, 'A')



## output
# Edges in MST:
# Visited A with cost 0
# Visited B with cost 2
# Visited C with cost 3
# Visited E with cost 5
# Visited D with cost 6
# Total Cost of MST: 16