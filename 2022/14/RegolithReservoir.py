from operator import add, sub

lines = open("input").readlines()
lines = [[tuple(map(int, x.split(","))) for x in s.split("->")] for s in lines]
world = {}
floor = max((y for line in lines for _, y in line))
for line in lines:
    for i in range(1, len(line)):
        a, b = line[i - 1], line[i]
        diff = tuple(map(lambda a, b: ((x := b - a), x and x // abs(x) or 0)[-1], a, b))
        while a != b:
            world[a] = "#"
            a = tuple(map(add, a, diff))
        world[a] = "#"

# fmt: off
def drop(has_floor):
    x, y = 500, 0
    while True:
        if y > floor:
            if has_floor: world[(x, y)] = "o"; return (x, y)
            else: return False
        if not world.get((x, y + 1)):
            y += 1
        elif not world.get((x - 1, y + 1)):
            x -= 1; y += 1
        elif not world.get((x + 1, y + 1)):
            x += 1; y += 1
        else:
            world[(x, y)] = "o"; return (x, y)
# fmt: on


orig = world.copy()
while drop(False):
    pass
count = lambda: len([a for a, b in world.items() if b == "o"])
print(count())

world = orig
while last := drop(True) != (500, 0):
    pass
print(count())
