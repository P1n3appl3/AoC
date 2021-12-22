state = set()
with open("test") as f:
    key = [1 if c == "#" else 0 for c in f.readline()]
    f.readline()
    for y, l in enumerate(f):
        for x, c in enumerate(l):
            if c == "#":
                state.add((x, y))

symbols = (".", "#")
nums = ("0", "1")
neighbors = lambda x, y: [(x + a, y + b) for b in range(-1, 2) for a in range(-1, 2)]
lookup = lambda x, y: key[int("".join(nums[n in state] for n in neighbors(x, y)), 2)]


def bounding_box(points):
    xs, ys = zip(*points)
    return (min(xs), min(ys), max(xs), max(ys))


def step(inv=False):
    new = set()
    l, t, r, b = bounding_box(state)
    for y in range(t - 1, b + 2):
        for x in range(l - 1, r + 2):
            if inv != lookup(x, y):
                new.add((x, y))
    return new


def display(inv=False):
    l, t, r, b = bounding_box(state)
    for y in range(t - 1, b + 2):
        for x in range(l - 1, r + 2):
            print(symbols[inv != ((x, y) in state)], end="")
        print()


# display()
for i in range(2):
    state = step(i % 2 == 0)
    print(len(state))
    # display(i % 2 == 0)
