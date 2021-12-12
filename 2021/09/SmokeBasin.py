from operator import mul
from functools import reduce as fold

grid = [[int(c) for c in line.strip()] for line in open("input").readlines()]
h = len(grid)
w = len(grid[0])


def fill(x, y, v):
    if not (0 <= x < w and 0 <= y < h) or grid[y][x] == 9 or v[y][x]:
        return 0
    v[y][x] = True
    return (
        1
        + fill(x, y + 1, v)
        + fill(x, y - 1, v)
        + fill(x + 1, y, v)
        + fill(x - 1, y, v)
    )


total = 0
basins = []
for y in range(h):
    for x in range(w):
        n = grid[y][x]
        if (
            (y == 0 or n < grid[y - 1][x])
            and (y == h - 1 or n < grid[y + 1][x])
            and (x == 0 or n < grid[y][x - 1])
            and (x == w - 1 or n < grid[y][x + 1])
        ):
            total += n + 1
            basins.append(fill(x, y, [[False for _ in range(w)] for _ in range(h)]))
print(total)
print(fold(mul, sorted(basins)[-3:]))
