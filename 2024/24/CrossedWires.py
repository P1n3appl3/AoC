from collections import deque
from operator import or_, and_, xor


with open("input") as f:
    initial, allgates = f.read().split("\n\n")

values = {name: int(val) for name, val in [s.split(":") for s in initial.splitlines()]}
gates = deque()
for g in allgates.splitlines():
    l, op, r, _, out = g.split()
    gates.append((l, r, {"AND": and_, "OR": or_, "XOR": xor}[op], out))

while len(gates) > 0:
    if not any(g[3].startswith("z") for g in gates):
        break
    (l, r, op, out) = cur = gates.popleft()
    if l in values and r in values:
        values[out] = op(values[l], values[r])
    else:
        gates.append(cur)

extract = lambda l: ((int(k[1:]), v) for k, v in values.items() if k.startswith(l))
num = lambda name: sum([b * 2**i for i, b in sorted(extract(name))])

print(num("z"))

print(f"{num("z"):048b}")
x = num("x")
y = num("y")
print(f"{x+y:048b}")
print()
print(f"{x:048b}")
print(f"{y:048b}")

"""
s0 = x0^y0
c0 = x0&y0
s1 = c0^(x1^y1)
c1 = x0&y0
s2 = c1^(x2^y2)
"""
