#5 shortest path (matrix)
from collections import deque
def sp(n, m, grid, s, e):
    if not (0 <= s[0] < n and 0 <= s[1] < m and 0 <= e[0] < n and 0 <= e[1] < m) or grid[s[0]][s[1]] or grid[e[0]][e[1]]:
        return None
    q = deque([(s[0], s[1], 0, [])])
    v = {s}
    while q:
        x, y, d, path = q.popleft()
        current_path = path + [(x, y)]
        if (x, y) == e:
            return d, current_path
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not grid[nx][ny] and (nx, ny) not in v:
                v.add((nx, ny))
                q.append((nx, ny, d + 1, current_path))
    return None
