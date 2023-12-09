from functools import reduce
from math import ceil, sqrt
from operator import mul

quad = lambda a, b, c: (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
solve = lambda t, d: 1 + t - 2 * ceil(quad(-1, t, -d - 1))

with open("input") as f:
    times = [int(s) for s in f.readline().split(":")[-1].split()]
    dists = [int(s) for s in f.readline().split(":")[-1].split()]

print(reduce(mul, (solve(*p) for p in zip(times, dists))))

time = int("".join(map(str, times)))
dist = int("".join(map(str, dists)))
print(solve(time, dist))
