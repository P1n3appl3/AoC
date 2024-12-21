from functools import cache

with open("input") as f:
    codes = f.read().splitlines()
pad = lambda s: {
    c: (x, y)
    for y, line in enumerate(s.splitlines())
    for x, c in enumerate(line)
}
numpad = pad("789\n456\n123\n.0A")
dirpad = pad(".^A\n<v>")
diff = lambda a, b: (b[0] - a[0], b[1] - a[1])
strip_num = lambda s: int("".join((c for c in s if c.isdigit())))


@cache
def shortest(s, target, level=-1):
    if level == target:
        return len(s)
    cur = numpad["A"] if level < 0 else dirpad["A"]
    total = 0
    for c in s:
        dx, dy = diff(cur, new := numpad[c] if level < 0 else dirpad[c])
        hori = ("<" if dx < 0 else ">") * abs(dx)
        vert = ("^" if dy < 0 else "v") * abs(dy)
        recurse = lambda s: shortest(s + "A", target, level + 1)
        a, b = recurse(hori + vert), recurse(vert + hori)
        if    (level <  0 and cur[0] == 0 and new[1] == 3
            or level >= 0 and cur[0] == 0 and new[1] == 0):
            total += a
        elif  (level <  0 and cur[1] == 3 and new[0] == 0
            or level >= 0 and cur[1] == 0 and new[0] == 0):
            total += b
        else:
            total += min(a, b)
        cur = new
    return total


solve = lambda n: sum((shortest(code, n) * strip_num(code) for code in codes))
print(solve(2))
print(solve(25))
