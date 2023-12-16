import re
from itertools import cycle

with open("small2") as f:
    directions = f.readline().strip()
    f.readline()
    paths = {}
    for line in f:
        name, l, r = re.findall(r"(...) = \((...), (...)\)", line)[0]
        paths[name] = (l, r)

cur = "AAA"
for i, c in enumerate(cycle(directions), start=1):
    cur = paths[cur][c == "R"]
    if cur == "ZZZ":
        print(i)
        break

starts = [s for s in paths.keys() if s.endswith("A")]
found = [[] for _ in range(len(starts))]

for s in starts:
    t = (-1, "AAA")
    h = (0, paths["AAA"][directions[0] == "R"])
    while t != h:
        i, t = t
        j, h = h
        i = i + 1 % len(directions)
        t = (i, paths[t][directions[i] == "R"])
        t = (i + 1, paths[t][directions[i + 1] == "R"])
    print(t, h)

    # for i in cycle(range(len(directions)))
    # for s in range(len(starts)):
    #     starts[s] = paths[starts[s]][c == "R"]
    #     if starts[s].endswith("Z"):
    #         found[s].append(i % len(directions))
    # if i > 10000:
    #     break
print(found)
print(starts)
