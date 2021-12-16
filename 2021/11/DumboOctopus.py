from itertools import product

grid = [[int(c) for c in line.strip()] for line in open("input").readlines()]
s = len(grid)


def display(grid):
    print()
    for l in grid:
        print("".join(map(str, l)).replace("0", "\x1b[1m0\x1b[0m"))


def get_neighbors(x, y):
    results = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            a, b = x + i, y + j
            if not (0 <= a < s and 0 <= b < s):
                continue
            results.append((a, b))
    return results


points = list(product(range(s), range(s)))
neighbors = {p: get_neighbors(p[0], p[1]) for p in points}
flashes = 0
# display(grid)

for i in range(1, 1_000_000):
    for x, y in points:
        grid[x][y] += 1

    prev = -1
    flashed = [[False for _ in range(s)] for _ in range(s)]
    while flashes != prev:
        prev = flashes
        for x, y in points:
            if not flashed[x][y] and grid[x][y] > 9:
                flashes += 1
                flashed[x][y] = True
                for a, b in get_neighbors(x, y):
                    grid[a][b] += 1
    for x, y in points:
        if flashed[x][y]:
            grid[x][y] = 0

    if i == 100:
        print(flashes)

    if all((all(l) for l in flashed)):
        print(i)
        break
    # display(grid)
