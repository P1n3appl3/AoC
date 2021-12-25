import re

steps = []
with open("test") as f:
    for l in f:
        on = len(l.split()[0]) == 2
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", l))
        steps.append((on, ((x1, x2), (y1, y2), (z1, z2))))

for s in steps:
    print(s)
