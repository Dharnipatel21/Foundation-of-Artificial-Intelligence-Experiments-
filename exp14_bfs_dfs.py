#14 BFS- DFS problem
from collections import deque
# Algorithm: BFS uses queue (FIFO), DFS uses recursion (LIFO)
# Use Case: Social network pathfinding
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
def bfs(g, start, goal):
    q, visited = deque([[start]]), {start}
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal: return path
        for n in g[node]:
            if n not in visited:
                visited.add(n)
                q.append(path + [n])
def dfs(g, node, goal, visited=set(), path=[]):
    if node in visited: return None
    visited.add(node)
    path = path + [node]
    if node == goal: return path
    for n in g[node]:
        result = dfs(g, n, goal, visited, path)
        if result: return result
print("BFS:", bfs(graph, 'A', 'F'))
print("DFS:", dfs(graph, 'A', 'F'))
BFS: ['A', 'C', 'F']
DFS: ['A', 'B', 'E', 'F']
