from itertools import product, count
from functools import reduce
from operator import or_, add

lines = open("input").readlines()
width, height = len(lines[0]) - 3, len(lines) - 2
start = (lines[0].index(".") - 1, -1)
end = (lines[-1].index(".") - 1, height)
spaces = set(product(range(width), range(height))) | {start, end}
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0))
arrows = "><v^"
bliz = [[] for i in range(4)]
for y in range(height):
    for x in range(width):
        if (c := lines[y + 1][x + 1]) != ".":
            bliz[arrows.index(c)].append((x, y))


def show(bliz, touched):
    for y in range(-1, height + 1):
        for x in range(-1, width + 1):
            c = "." if (x, y) in spaces else "#"
            for i in range(4):
                if (x, y) in bliz[i]:
                    if c in arrows:
                        c = "2"
                    elif c == "2":
                        c = "3"
                    else:
                        c = arrows[i]
            if (x, y) in touched:
                c = "E"
            print(c, end="")
        print()
    print()


def search(cur, to, time):
    touched = {cur}
    # show(bliz, touched)
    for time in count(time + 1):
        for i in range(4):
            dx, dy = dirs[i]
            for j in range(len(bliz[i])):
                x, y = bliz[i][j]
                bliz[i][j] = ((x + dx + width) % width, (y + dy + height) % height)

        new = set()
        for pos in touched:
            new |= {tuple(map(add, pos, d)) for d in dirs} & spaces
        new -= reduce(or_, map(set, bliz))

        touched = new
        # show(bliz, touched)
        if to in touched:
            return time


print(there := search(start, end, 0))
back = search(end, start, there)
print(search(start, end, back))
