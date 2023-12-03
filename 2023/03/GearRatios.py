import re
from itertools import product

nums, num_grid = [], {}
parts, gears = set(), set()
for row, line in enumerate(open("input")):
    for m in re.finditer(r"\d+", line):
        col, size = m.start(), m.end() - m.start()
        num_grid |= {(row, col + i): len(nums) for i in range(size)}
        num_grid[pos := (row, m.start())] = len(nums)
        nums.append(((row, col), int(line[m.start() : m.end()]), size))
    for m in re.finditer(r"[^\d\s.]", line):
        parts.add(pos := (row, m.start()))
        if line[m.start()] == "*":
            gears.add(pos)


rect = lambda r, c, l: set(product(range(r - 1, r + 2), range(c - 1, c + l + 1)))
print(sum(n for (row, col), n, l in nums if bool(rect(row, col, l) & parts)))

s = 0
for row, col in gears:
    n = set(num_grid[(r, c)] for r, c in rect(row, col, 1) if (r, c) in num_grid)
    print(n)
    match list(n):
        case [a, b]:
            s += nums[a][1]*nums[b][1]
print(s)
