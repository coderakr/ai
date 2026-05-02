# Implement Greedy search algorithm for Single-Source Shortest Path Problem

import heapq

def dijkstra(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority Queue (min-heap)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if already found a better path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Greedy relaxation step
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# ---------------- Graph ----------------
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

# ---------------- Main ----------------
start_node = 'A'
result = dijkstra(graph, start_node)

print("Shortest distances from source:", start_node)
for node, dist in result.items():
    print(f"{node} : {dist}")




## output
# Shortest distances from source: A
# A : 0
# B : 3
# C : 1
# D : 8
# E : 10
# F : 13