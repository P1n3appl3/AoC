import re
from operator import add, sub

board, steps = open("small").read().split("\n\n")
spaces = {}
cur = None
for r, row in enumerate(board.splitlines()):
    for c, char in enumerate(row):
        if char != " ":
            spaces[(r + 1, c + 1)] = char
            if not cur:
                cur = (r + 1, c + 1)


def move(pos, dir, times):
    diff = ((0, 1), (1, 0), (0, -1), (-1, 0))[dir]
    for _ in range(times):
        new = tuple(map(add, pos, diff))
        if not (s := spaces.get(new)):
            while True:
                new = tuple(map(sub, new, diff))
                if not (s := spaces.get(new)):
                    new = tuple(map(add, new, diff))
                    s = spaces.get(new)
                    break
        # print(" ", new, s)
        if s == "#":
            return pos
        pos = new
    return pos


num = [int(s) for s in re.split("R|L", steps)]
let = [(s == "R") * 2 - 1 for s in re.split("\d+", steps.strip()) if s] + [0]
dir = 0
for n, turn in zip(num, let):
    # print(cur, dir, n, turn)
    cur = move(cur, dir, n)
    dir = (dir + 4 + turn) % 4
# print(cur, dir, n, turn)

print(1000 * cur[0] + 4 * cur[1] + dir)
