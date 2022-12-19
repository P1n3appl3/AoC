from operator import mul
from functools import reduce
from itertools import product


def seen(l, n):  # TODO: "takewhile" + 1?
    viz = 0
    for x in l:
        viz += 1
        if x >= n:
            break
    return viz


grid = [[int(x) for x in line.strip()] for line in open("input")]
size = len(grid)
trans = [[grid[x][y] for x in range(size)] for y in range(size)]
total = size * 4 - 4
maxviz = 0
neighbors = lambda x, y: (
    grid[x][:y][::-1],
    grid[x][y + 1 :],
    trans[y][:x][::-1],
    trans[y][x + 1 :],
)

for x, y in product(range(1, size - 1), repeat=2):
    a = grid[x][y]
    adj = neighbors(x, y)
    total += any(max(n) < a for n in adj)
    maxviz = max(maxviz, reduce(mul, (seen(n, a) for n in adj)))


print(total)
print(maxviz)
