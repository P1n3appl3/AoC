import heapq
import sys

grid = [[int(c) for c in line.strip()] for line in open("input").readlines()]
h = len(grid)
w = len(grid[0])
inside = lambda x, y: 0 <= x < w and 0 <= y < h
inside_big = lambda x, y: 0 <= x < w * 5 and 0 <= y < h * 5
get_neighbors = lambda x, y, i: [
    (x + a, y + b) for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)] if i(x + a, y + b)
]
pri = [(0, 0, 0)]
best = [[sys.maxsize for _ in range(w)] for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

count = 0
while len(pri) > 0:
    cost, x, y = heapq.heappop(pri)
    visited[y][x] = True
    if (x, y) == (w - 1, h - 1):
        print(cost)
        break
    for a, b in get_neighbors(x, y, inside):
        if visited[b][a]:
            continue
        new = grid[b][a] + cost
        if new < best[b][a]:
            best[b][a] = new
            heapq.heappush(pri, (new, a, b))

pri = [(0, 0, 0)]
best = [[sys.maxsize for _ in range(w * 5)] for _ in range(h * 5)]
visited = [[False for _ in range(w * 5)] for _ in range(h * 5)]
wrap = lambda x: x if x < 10 else x - 9

while len(pri) > 0:
    cost, x, y = heapq.heappop(pri)
    visited[y][x] = True
    if (x, y) == (w * 5 - 1, h * 5 - 1):
        print(cost)
        break
    for a, b in get_neighbors(x, y, inside_big):
        if visited[b][a]:
            continue
        new = wrap(grid[b % h][a % w] + a // w + b // h) + cost
        if new < best[b][a]:
            best[b][a] = new
            heapq.heappush(pri, (new, a, b))

# for y in range(h * 5):
#     for x in range(w * 5):
#         print(wrap(grid[y % h][x % w] + x // w + y // h), end="")
#     print()
