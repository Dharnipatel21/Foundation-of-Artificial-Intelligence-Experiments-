#13 traveling salesman problem
import numpy as np
distances = np.array(
    [
        [0, 4, 8, 6],
        [8, 5, 3, 3],
        [4, 0, 5, 7],
        [6, 7, 3, 0],
    ]
)
def tsp_nearest_neighbor(dist, start=0):
    n = len(dist)
    visited = [False] * n
    route = [start]
    visited[start] = True
    total = 0
    current = start
    for _ in range(n - 1):
        nearest = -1
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and dist[current][city] < min_dist:
                min_dist = dist[current][city]
                nearest = city
        route.append(nearest)
        visited[nearest] = True
        total += min_dist
        current = nearest
    total += dist[current][start]  # Return to start
    route.append(start)
    return route, total
route, distance = tsp_nearest_neighbor(distances)
print("Optimized Route:", route)
print("Total Distance:", distance)
