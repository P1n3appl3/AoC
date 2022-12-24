points = {tuple(map(int, l.split(","))) for l in open("input")}
total = 0
adj = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
neighbors = lambda p: tuple((p[0] + x, p[1] + y, p[2] + z) for x, y, z in adj)
for p in points:
    total += sum(n not in points for n in neighbors(p))
print(total)
visited = set()
q = {(0, 0, 0)}
total = 0
while q:
    p = q.pop()
    visited.add(p)
    for n in neighbors(p):
        if n in visited or any(i not in range(-1, 21) for i in n):
            continue
        if n in points:
            total += 1
            continue
        q.add(n)
print(total)
