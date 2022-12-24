from itertools import cycle

shapes = (
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
)

locked = set(shapes[0]) | {(4, 0), (5, 0)}
translate = lambda p, d: tuple((x + d[0], y + d[1]) for x, y in p)
valid = lambda piece: all(p not in locked and p[0] in range(7) for p in piece)
highest = 0
count = 0
cur = translate(shapes[0], (2, 4))

# def show():
#     for y in range(1, highest + 5)[::-1]:
#         for x in range(7):
#             c = "."
#             if (x, y) in locked:
#                 c = "#"
#             if (x, y) in cur:
#                 c = "@"
#             print(c, end="")
#         print()
#     print()

heights = [0]
for d in cycle(open("input").read()[:-1]):
    trans = translate(cur, ((d == ">") * 2 - 1, 0))
    if valid(trans):
        cur = trans
    drop = translate(cur, (0, -1))
    if valid(drop):
        cur = drop
    else:
        for p in cur:
            locked.add(p)
        count += 1
        highest = max(highest, max(y for _, y in cur))
        heights.append(highest)
        if count == 2022:
            print(highest)
        if count == 10000:
            break
        cur = translate(shapes[count % 5], (2, highest + 4))
diffs = [heights[i + 1] - heights[i] for i in range(len(heights) - 1)]

left, right = 100, 101  # in case the start isn't periodic cuz of the floor?
while right < 10000:
    if diffs[left] == diffs[right]:
        for i in range(5000):
            if diffs[left + i] != diffs[right + i]:
                break
        else:
            print("cycle detected with period", period := right - left)
            break
    right += 1

goal = 1_000_000_000_000
cyclediff = sum(diffs[left:right])
repeats = (goal - left) // period
togo = goal - (left + repeats * (right - left))
print(heights[left] + cyclediff * repeats + sum(diffs[left : left + togo]))
