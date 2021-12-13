from collections import defaultdict

paths = defaultdict(list)
with open("input") as f:
    for line in f:
        l, r = line.strip().split("-")
        if r != "start" and l != "end":
            paths[l].append(r)
        if l != "start" and r != "end":
            paths[r].append(l)

# for p in paths.items():
#     print(p)
routes = set()


def visit(current, hist, used):
    hist = hist + (current,)
    p = paths[current]
    if current == "end":
        routes.add(hist)
        return
    for next in p:
        if next.islower() and next in hist:
            if not used:
                visit(next, hist, True)
        else:
            visit(next, hist, used)


visit("start", (), True)
# print()
# for r in sorted(routes):
#     print(','.join(r))
print(len(routes))
routes.clear()
visit("start", (), False)
# print()
# for r in sorted(routes):
#     print(",".join(r))
print(len(routes))
