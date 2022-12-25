from itertools import count
from operator import add
from collections import defaultdict


def size(elves):
    return (
        (min(x for x, _ in elves), min(y for _, y in elves)),
        (max(x for x, _ in elves), max(y for _, y in elves)),
    )


def show(elves):
    (x0, y0), (x1, y1) = size(elves)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            print("#" if (x, y) in elves else ".", end="")
        print()
    print()


elves = set()
neighbors = tuple((x, y) for y in range(-1, 2) for x in range(-1, 2) if x or y)
dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
checks = (((-1, 0), (0, 0), (1, 0)), ((0, -1), (0, 0), (0, 1)))
for y, line in enumerate(open("input")):
    for x, c in enumerate(line):
        if c == "#":
            elves.add((x, y))
# show(elves)

dir = 0
for i in count(1):
    moves = defaultdict(list)
    moved = False
    for e in elves:
        if not any(tuple(map(add, e, n)) in elves for n in neighbors):
            continue
        for j in range(4):
            pos = tuple(map(add, e, dirs[(dir + j) % 4]))
            if not any(
                tuple(map(add, pos, c)) in elves for c in checks[(dir + j) % 4 // 2]
            ):
                moves[pos].append(e)
                break
    for k, v in moves.items():
        if len(v) == 1:
            moved = True
            elves.remove(v[0])
            elves.add(k)
    dir += 1
    if i == 10:
        (x0, y0), (x1, y1) = size(elves)
        print((y1 - y0 + 1) * (x1 - x0 + 1) - len(elves))
    if not moved:
        print(i)
        break
