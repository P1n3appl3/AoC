from collections import defaultdict
from itertools import combinations

with open("input") as f:
    raw = f.read()

con = defaultdict(set)
for line in raw.splitlines():
    l, r = line.split("-")
    con[l].add(r)
    con[r].add(l)
con = {k: v | {k} for k, v in con.items()}


threes = set()
for g in con.values():
    for c in combinations(g, 3):
        if all(set(c) <= con[machine] for machine in c) and any(
            machine.startswith("t") for machine in c
        ):
            threes.add(tuple(sorted(c)))
print(len(threes))


def biggest(g):
    for n in range(4, len(g))[::-1]:
        for c in combinations(g, n):
            if all(set(c) <= con[machine] for machine in c):
                return c
    return set()


print(",".join(sorted(max([biggest(g) for g in con.values()], key=len))))
