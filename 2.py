# Implement A star Algorithm for any game search problem.
import heapq

# Heuristic function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def a_star(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # Priority Queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        # Goal reached
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Explore neighbors (4 directions)
        neighbors = [
            (current[0]+1, current[1]),
            (current[0]-1, current[1]),
            (current[0], current[1]+1),
            (current[0], current[1]-1)
        ]

        for neighbor in neighbors:
            r, c = neighbor

            # Check bounds and obstacles
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                temp_g = g_cost[current] + 1

                if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                    g_cost[neighbor] = temp_g
                    f_cost = temp_g + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None


# ---------------- Main ----------------

# 0 = free path, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = a_star(grid, start, goal)

print("Shortest Path:", path)