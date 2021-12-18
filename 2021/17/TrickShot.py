import re
from collections import defaultdict

l, r, b, t = map(int, re.findall(r"-?\d+", open("input").read()))
inside = lambda x, y: l <= x <= r and b <= y <= t
past = lambda x, y, v: x > r or y < b and v <= 0


def shot(vx, vy):
    pos = (0, 0)
    yield pos
    while not past(*pos, vy) and not inside(*pos):
        pos = (pos[0] + vx, pos[1] + vy)
        vx = max(vx - 1, 0)
        vy -= 1
        yield pos


def display(vx, vy):
    points = list(shot(vx, vy))
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    for j in range(min(b, min(ys)), max(t, max(ys)) + 1)[::-1]:
        for i in range(max(r, max(xs)) + 1):
            current = " "
            if (i, j) in points:
                current = "#"
            elif inside(i, j):
                current = "T"
            print(current, end="")
        print()
    print("-" * 80)


# display(7, 2)
# display(6, 3)
# display(9, 0)
# display(17, -4)
# display(6, 9)
# display(6, 9)
# display(7, 9)

# while True:
#     vx, vy = map(int, input("input 'vx,vy': ").split(","))
#     display(vx, vy)


lowest_vx = round((1 + (1 + 8 * l) ** 0.5) / 2 - 1)
slowest_shot = list(shot(lowest_vx, -b - 1))
print(max(y for _, y in slowest_shot))
max_len = len(slowest_shot)


def x_shot(vx):
    x = 0
    i = 0
    result = []
    while x < l and vx > 0:
        i += 1
        x += vx
        vx = max(0, vx - 1)
    while l <= x <= r and vx > 0:
        result.append(i)
        i += 1
        x += vx
        vx = max(0, vx - 1)
    if vx == 0 and l <= x <= r:
        result += list(range(i, max_len + 1))
    return result


def y_shot(vy):
    y = 0
    i = 0
    result = []
    while y > t or vy > 0:
        i += 1
        y += vy
        vy -= 1
    while b <= y <= t:
        result.append(i)
        i += 1
        y += vy
        vy -= 1
    return result


shot_len = {i: x_shot(i) for i in range(lowest_vx, r + 1)}
inv_len = defaultdict(list)
for k, l in shot_len.items():
    for v in l:
        inv_len[v].append(k)
# for i in sorted(inv_len.items()):
#     print(i)

shot_height = {i: y_shot(i) for i in range(b, -b)}
inv_height = defaultdict(list)
for k, l in shot_height.items():
    for v in l:
        inv_height[v].append(k)
# print()
# for i in sorted(inv_height.items()):
#     print(i)

results = set()
for i in range(max_len + 1):
    for l in inv_len[i]:
        for h in inv_height[i]:
            results.add((l, h))
# print(sorted(results))
print(len(results))

# ans = open("test_answers").read().split()
# ans = sorted([tuple(map(int, s.split(","))) for s in ans])
# print(ans)
