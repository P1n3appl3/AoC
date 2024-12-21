from functools import cache

with open("input") as f:
    raw = f.read()
numpad = {
    c: (x, y)
    for y, line in enumerate("789\n456\n123\n.0A".splitlines())
    for x, c in enumerate(line)
}
dirpad = {
    c: (x, y)
    for y, line in enumerate(".^A\n<v>".splitlines())
    for x, c in enumerate(line)
}
codes = raw.splitlines()

dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
diff = lambda a, b: (b[0] - a[0], b[1] - a[1])


@cache
def move(s, p2=False, level=0):
    if not p2 and level == 2 or p2 and level == 25:
        return s
    pos = dirpad["A"]
    path = ""
    for c in s:
        new = dirpad[c]
        dx, dy = diff(pos, new)
        hori = "<" if dx < 0 else ">"
        vert = "^" if dy < 0 else "v"
        a = move(hori * abs(dx) + vert * abs(dy) + "A", p2, level + 1)
        b = move(vert * abs(dy) + hori * abs(dx) + "A", p2, level + 1)
        if pos[0] == 0 and new[1] == 0:
            path += a
        elif pos[1] == 0 and new[0] == 0:
            path += b
        else:
            path += a if len(a) < len(b) else b
        pos = new
    return path


def solve(p2):
    ans = 0
    for code in codes:
        print(".", end="")
        path = ""
        pos = numpad["A"]
        for c in code:
            new = numpad[c]
            dx, dy = diff(pos, new)
            hori = "<" if dx < 0 else ">"
            vert = "^" if dy < 0 else "v"
            a = move(abs(dx) * hori + abs(dy) * vert + "A", p2)
            b = move(abs(dy) * vert + abs(dx) * hori + "A", p2)
            if pos[0] == 0 and new[1] == 3:
                path += a
            elif pos[1] == 3 and new[0] == 0:
                path += b
            else:
                path += a if len(a) < len(b) else b
            pos = numpad[c]
        ans += len(path) * int("".join((c for c in code if c.isdigit())))
    print()
    return ans


print(solve(False))
print(solve(True))
