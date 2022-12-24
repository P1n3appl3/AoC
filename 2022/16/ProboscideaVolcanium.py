import re
from collections import deque

p = re.compile("Valve (..).*=(\d+);.*valves? (.*)")

rates = {}
adj = {}
for line in open("input"):
    cur, rate, paths = p.match(line).groups()
    rates[cur] = int(rate)
    adj[cur] = paths.split(", ")

# # dot
# print("strict graph D {")
# for v, paths in adj.items():
#     # if not rates[v]:
#     #     print(v, '[style="invis"]')
#     print(v, "--", f' {{{" ".join(paths)}}} ')
# print("}")
# import sys; sys.exit()

# is there a better way than BFS from every node?
# is repeatedly squaring the adjacency matrix cheaper?
dists = {}
for v in rates:
    if not rates[v] and v != "AA":
        continue
    visited = {v}
    q = deque([(n, 1) for n in adj[v]])
    costs = {}
    while q:
        cur, cost = q.popleft()
        visited.add(cur)
        if rates[cur]:
            costs[cur] = cost
        for n in adj[cur]:
            if n not in visited:
                q.append((n, cost + 1))
    dists[v] = costs

# # dot
# print("strict graph D {")
# print('layout="circo"')
# for v, paths in dists.items():
#     for p,weight in paths.items():
#         if weight == 1:
#             print(v, "--", p)
#         else:
#             print(v, "--", p, f'[label="{weight}"]')
# print("}")
# import sys; sys.exit()


def solve(cur, time, score, opened):
    # print(cur, time, score, opened)
    best = score
    for n, dist in dists[cur].items():
        if n in opened or dist >= time - 1:
            continue
        t = time - dist - 1
        best = max(best, solve(n, t, score + t * rates[n], opened | {n}))
    return best


print(solve("AA", 30, 0, {"AA"}))


def double(me_t, me, el_t, el, time, score, to_open):
    if not time:
        return score
    score += time * (rates[me] * (not me_t) + rates[el] * (not el_t))
    best = score
    t = time - 1
    if not me_t:
        for v in to_open:
            if dists[me][v] >= t:
                continue
            new = to_open - {v}
            if not el_t:
                for n in new:
                    if dists[el][n] >= t:
                        continue
                    tmp = double(dists[me][v], v, dists[el][n], n, t, score, new - {n})
                    best = max(tmp, best)
            else:
                tmp = double(dists[me][v], v, el_t - 1, el, t, score, new)
                best = max(tmp, best)
    elif not el_t:
        for v in to_open:
            if dists[el][v] >= t:
                continue
            new = to_open - {v}
            tmp = double(me_t - 1, me, dists[el][v], v, t, score, new)
            best = max(tmp, best)
    best = max(best, double(me_t - 1, me, el_t - 1, el, t, score, to_open))
    return best


print(double(0, "AA", 0, "AA", 26, 0, set(dists) - {"AA"}))
