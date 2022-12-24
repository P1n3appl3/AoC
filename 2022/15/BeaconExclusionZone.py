import re
from functools import reduce
from collections import defaultdict

p = re.compile(".*x=(.+), y=(.+):.*x=(.+), y=(.+)")
combine = lambda a, b: (min(a[0], b[0]), max(a[1], b[1]))
intersect = lambda a, b: (max(a[0], b[0]), min(a[1], b[1]))
overlap = lambda a, b: a[1] >= b[0] and a[0] <= b[1]


def add(new, ranges):
    x, y = new
    overlapping = {new}
    for r in ranges:
        a, b = r
        if a <= x and b >= y:
            return
        if y < a - 1 or x > b + 1:
            continue
        overlapping.add(r)
    ranges -= overlapping
    new = reduce(combine, overlapping)
    ranges.add(new)


target = 4_000_000
rows = [set() for _ in range(target + 1)]
beacons = set()
for line in open("input"):
    a, b, x, y = map(int, p.match(line).groups())
    size = abs(a - x) + abs(b - y)
    vert = intersect((b - size, b + size), (0, target))
    for i in range(vert[0], vert[1] + 1):
        diff = abs(size - abs(b - i))
        add((a - diff, a + diff), rows[i])
    if y == target // 2:
        beacons.add(y)

print(sum((b - a + 1 for a, b in rows[target // 2])) - len(beacons))
for i in range(target + 1):
    inside = sorted(filter(lambda r: overlap(r, (0, target)), rows[i]))
    if len(inside) > 1:
        print(i + (inside[0][1] + 1) * target)
