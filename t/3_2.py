# Implement Greedy search algorithm for Kruskal's Minimal Spanning Tree Algorithm

# Find with path compression
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

# Union by rank
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(vertices, edges):
    # Sort edges by weight (Greedy step)
    edges.sort(key=lambda x: x[2])

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        # Check if adding edge forms a cycle
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# ---------------- Main ----------------
vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 2),
    ('A', 'D', 6),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('B', 'E', 5),
    ('C', 'E', 7),
    ('D', 'E', 9)
]

mst, cost = kruskal(vertices, edges)

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Cost of MST:", cost)