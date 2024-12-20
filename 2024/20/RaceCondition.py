from heapq import heappop, heappush
from collections import Counter

board = set()
start = end = (0, 0)
with open("input") as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line):
            pos = (x, y)
            match c:
                case ".":
                    board.add(pos)
                case "S":
                    board.add(pos)
                    start = pos
                case "E":
                    board.add(pos)
                    end = pos

dists = {}
todo = [(0, end)]
while todo:
    n, pos = heappop(todo)
    dists[pos] = n
    x, y = pos
    for new in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        if new in board and new not in dists:
            heappush(todo, (n + 1, new))

p1 = Counter()
p2 = Counter()

dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
manhattan = lambda n: {
    (x, y)
    for x in range(-n, n + 1)
    for y in range(-n, n + 1)
    if 1 < dist((0, 0), (x, y)) <= n
}

m2 = manhattan(2)
m20 = manhattan(20)
for x, y in board:
    start = (x, y)
    for dx, dy in m2:
        pos = (x + dx, y + dy)
        if pos in board:
            saved = dists[start] - dists[pos] - dist(start, pos)
            p1[saved] += saved > 0
    for dx, dy in m20:
        pos = (x + dx, y + dy)
        if pos in board:
            saved = dists[start] - dists[pos] - dist(start, pos)
            p2[saved] += saved > 0

# for k, v in sorted(((k, v) for k, v in p2.items() if k >= 50)):
#     print(f"• There are {v} cheats that save {k} picoseconds")
print(sum((v for k, v in p1.items() if k >= 100)))
print(sum((v for k, v in p2.items() if k >= 100)))
