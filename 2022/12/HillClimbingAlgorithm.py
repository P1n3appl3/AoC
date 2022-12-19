from itertools import product, count
from collections import deque

grid = open("input").read().splitlines()
nodes = set(product(range(len(grid)), range(len(grid[0]))))
for y, x in nodes:
    if grid[y][x] == "S":
        end = (y, x)
        grid[y] = grid[y][:x] + "a" + grid[y][x + 1 :]
    elif grid[y][x] == "E":
        start = (y, x)
        grid[y] = grid[y][:x] + "z" + grid[y][x + 1 :]

adj = {}
for y, x in nodes:
    neighbors = set()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        a = y + dy
        b = x + dx
        if (a, b) in nodes and ord(grid[y][x]) - 1 <= ord(grid[a][b]):
            neighbors.add((a, b))
    adj[(y, x)] = neighbors

# def showpath(path):
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             c = f"\x1b[1m{grid[y][x].upper()}\x1b[0m" if (y, x) in path else grid[y][x]
#             print(c, end="")
#         print()


def bfs(adj, cond):
    visited = {start: None}
    q = deque([(start, 0)])
    while q:
        cur, dist = q.popleft()
        if cond(cur):
            # path = [cur]
            # while cur := visited[cur]:
            #     path.append(cur)
            # showpath(path)
            return dist
        for n in adj[cur]:
            if n not in visited:
                visited[n] = cur
                q.append((n, dist + 1))


print(bfs(adj, lambda x: x == end))
print(bfs(adj, lambda x: grid[x[0]][x[1]] == "a"))
