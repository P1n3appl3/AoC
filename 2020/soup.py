import sys
import copy
from functools import reduce
import string
import itertools
from collections import defaultdict, deque

with open("input") as f:
    temp = f.read().split("\n\n")

p1 = deque(map(int,temp[0].split()[2:]))
p2 = deque(map(int,temp[1].split()[2:]))

while p1 and p2:
    x += 1
    a = p1.popleft()
    b = p2.popleft()
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)
if not p1:
    p1 = p2

print(sum(n * (i+1) for i,n in enumerate(list(p1)[::-1])))

sys.exit()

with open("myinput") as f:
    temp = f.read().split("\n\n")

# 0 1 2 3 == right down left up

tiles = set()
for tile in temp:
    _, title, *data = tile.split()
    n = int(title[:-1])
    l = len(data[0])
    r = "".join(data[-i - 1][-1] for i in range(l))
    d = data[-1]
    l = "".join(data[-i - 1][0] for i in range(l))
    u = data[0]
    flip = lambda x: x[::-1]
    tiles.add(
        (
            n,
            (  # rotations
                (r, d, l, u),
                (u, r, d, l),
                (l, u, r, d),
                (d, l, u, r),
                # flips (along y)
                (l, flip(d), r, flip(u)),
                (flip(u), l, flip(d), r),
                (r, flip(u), l, flip(d)),
                (flip(d), r, flip(u), l),
                # flops (along x)
                (flip(r), u, flip(l), d),
                (d, flip(r), u, flip(l)),
                (flip(l), d, flip(r), u),
                (u, flip(l), d, flip(r)),
            ),
        )
    )

corner = None
total = 1
for a in sorted(tiles):
    found = [False] * 4
    current = a[1][0]
    for b in tiles:
        if a == b:
            continue
        orientations = b[1]
        for o in orientations:
            if o[2] == current[0]:
                found[0] = True
            if o[3] == current[1]:
                found[1] = True
            if o[0] == current[2]:
                found[2] = True
            if o[1] == current[3]:
                found[3] = True
    if sum(found) == 2:
        if found == [True, False, False, True]:
            corner = a
        total *= a[0]

print(total)


class Wildcard(object):
    def __eq__(self, other):
        return True


size = int(len(tiles) ** 0.5)


def apply_constraint(board, tile, work, pos):
    x, y = pos
    r = range(0, size)
    if (x + 1, y) not in board and x + 1 in r:
        if type(work[(x + 1, y)][2]) is str:
            print("AHHHH")
            sys.exit()
        work[(x + 1, y)][2] = tile[0]
    if (x - 1, y) not in board and x - 1 in r:
        if type(work[(x - 1, y)][0]) is str:
            print("AHHHH")
            sys.exit()
        work[(x - 1, y)][0] = tile[2]
    if (x, y + 1) not in board and y + 1 in r:
        if type(work[(x, y + 1)][1]) is str:
            print("AHHHH")
            sys.exit()
        work[(x, y + 1)][1] = tile[3]
    if (x, y - 1) not in board and y - 1 in r:
        if type(work[(x, y - 1)][3]) is str:
            print("AHHHH")
            sys.exit()
        work[(x, y - 1)][3] = tile[1]


def dfs(board, tiles, work):
    if not tiles:
        return board
    if len(tiles) == 1:
        print()
        for k, v in sorted(board.items()):
            print(k, v)
        for thing in work.values():
            print([i if type(i) is str else None for i in thing])
        print(tiles)
        # sys.exit()
    # if len(tiles) % 2 == 0:
    #     print(" " * (len(tiles) // 2) + "X")
    potential = set(work.keys())
    for pos in potential:
        for tile in tiles:
            for o in tile[1]:
                if o == tuple(work[pos]):
                    newboard = copy.deepcopy(board)
                    newwork = copy.deepcopy(work)
                    newtiles = copy.deepcopy(tiles)

                    newtiles.remove(tile)
                    del newwork[pos]
                    newboard[pos] = (o, tile[0])
                    apply_constraint(newboard, o, newwork, pos)

                    finished = dfs(newboard, newtiles, newwork)
                    if finished:
                        return finished


n, orientations = corner
tiles.remove(corner)
board = {(0, 0): (orientations[0], n)}
work = defaultdict(lambda: [Wildcard()] * 4)
apply_constraint(board, board[(0, 0)][0], work, (0, 0))

board = dfs(board, tiles, work)

for b in board:
    print(b, board[b][1])

print(
    board[(0, 0)][1]
    * board[(0, size - 1)][1]
    * board[(size - 1, 0)][1]
    * board[(size - 1, size - 1)][1]
)

sys.exit()

with open("myinput") as f:
    lines, messages = f.read().split("\n\n")
    lines = lines.split("\n")
    messages = messages.split()

stuff = dict()
for line in lines:
    k, rest = line.split(":")
    k = int(k)
    rest = rest.split()

    if rest[0][0] == '"':
        stuff[k] = str(rest[0][1])
        continue

    stuff[k] = []
    temp = []
    for current in rest:
        if current == "|":
            stuff[k].append(temp)
            temp = []
        else:
            temp.append(int(current))
    stuff[k].append(temp)

print(stuff)
print(messages)


def validate(msg, rule, i):
    print(i, msg, stuff[rule])
    if type(stuff[rule]) is str:
        return msg[i] == rule
    for seq in stuff[rule]:
        temp = i
        good = True
        for r in seq:
            pass
            # if (i:=validate(msg, )) == -1
        # print(list((msg, r, i + n) for n, r in enumerate(seq)))
        if all(validate(msg, r, i + n) for n, r in enumerate(seq)):
            return True
    return False


print(validate(messages[0], 0, 0))
# print(sum(validate(msg, 0, 0) for msg in messages))


sys.exit()

with open("input") as f:
    lines = f.readlines()


def evaluate(tokens, lhs, i):
    if tokens[i] == "(":
        return evalexpr(tokens, i + 1)
    elif tokens[i] == "+":
        result, newi = evaluate(tokens, lhs, i + 1)
        return lhs + result, newi
    elif tokens[i] == "*":
        result, newi = evaluate(tokens, lhs, i + 1)
        while newi < len(tokens) and tokens[newi] == "+":
            result, newi = evaluate(tokens, result, newi)
        return lhs * result, newi
    else:
        return int(tokens[i]), i + 1


def evalexpr(tokens, i):
    acc = 0
    while i < len(tokens) and tokens[i] != ")":
        acc, i = evaluate(tokens, acc, i)
    return acc, i + 1


tokenize = lambda line: line.replace(")", " )").replace("(", "( ").split()
print(sum(evalexpr(tokenize(line), 0)[0] for line in lines))

# print(evalexpr(0)[0])

sys.exit()

with open("input") as f:
    lines = enumerate(map(str.strip, f.readlines()))

current = set()
for i, line in lines:
    for j, c in enumerate(line):
        if c == "#":
            current.add((0, 0, j, i))


def adj(pos):
    x, y, z = pos
    return set(
        (
            (i + x, j + y, k + z)
            for i in range(-1, 2)
            for j in range(-1, 2)
            for k in range(-1, 2)
            if any((i, j, k))
        )
    )


def adj4(pos):
    w, x, y, z = pos
    return set(
        (
            (h + w, i + x, j + y, k + z)
            for h in range(-1, 2)
            for i in range(-1, 2)
            for j in range(-1, 2)
            for k in range(-1, 2)
            if any((h, i, j, k))
        )
    )


for _ in range(6):
    neighbors = defaultdict(int)
    for pos in current:
        for n in adj4(pos):
            neighbors[n] += 1

    new_current = set()
    for pos, n in neighbors.items():
        if pos in current and 2 == n or n == 3:
            new_current.add(pos)

    current = new_current

print(len(current))

sys.exit()

with open("input") as f:
    raw = f.read()
    lines = raw.split("\n\n")

rules = dict()
kinds = []
departure_rules = []
for line in lines[0].split("\n"):
    temp = line.split("-")
    a = temp[0].split()[-1]
    b = temp[1].split()[0]
    c = temp[1].split()[-1]
    d = temp[2].split()[0]
    kind = temp[0].split(":")[0]
    rules[kind] = (range(int(a), int(b) + 1), range(int(c), int(d) + 1))
    kinds.append(kind)
    if kind.split()[0] == "departure":
        departure_rules.append(kind)

flatrules = [r for rule in rules.values() for r in rule]
yours = list(map(int, lines[1].split()[2].split(",")))
nearby = [list(map(int, x.split(","))) for x in lines[2].split()[2:]]
flatnearby = [n for near in nearby for n in near]


valid_tickets = []
total = 0
for near in nearby:
    rip = False
    for n in near:
        if not any(n in r1 or n in r2 for r1, r2 in rules.values()):
            total += n
            rip = True
            break
    if not rip:
        valid_tickets.append(near)

print(total)
nearby = valid_tickets

N = range(len(kinds))
possibilities = [set(kinds) for _ in N]
for near in nearby:
    for k, (r1, r2) in rules.items():
        for i in N:
            if near[i] not in r1 and near[i] not in r2:
                possibilities[i].discard(k)

cantbe = set()
answers = [0] * len(kinds)
stuff = sorted(enumerate(possibilities), key=lambda p: len(p[1]))
for p in stuff:
    i = p[0]
    answers[i] = p[1] - cantbe
    cantbe |= answers[i]
    answers[i] = answers[i].pop()

print(
    reduce(
        (lambda x, y: x * y),
        (yours[i] for i, k in enumerate(answers) if k.split()[0] == "departure"),
    )
)

sys.exit()

stuff = list(map(int, "8,13,1,0,18,9".split(",")))

current = stuff[-1]
stuff = {n: i for i, n in enumerate(stuff[:-1])}

N = 30000000
for i in range(len(stuff), N - 1):
    # print("turn", i, "- current:", current)
    to_add = current
    if current in stuff:
        # print("current was last seen at", stuff[current])
        current = i - stuff[current]
    else:
        current = 0
    stuff[to_add] = i

print(current)

sys.exit()

with open("input") as f:
    lines = f.readlines()

setbits = 0
clearbits = 0
mem = dict()
for line in lines:
    comp = line.split()
    if comp[0] == "mask":
        clearbits = ~int(
            comp[-1].replace("1", "X").replace("0", "1").replace("X", "0"), 2
        )
        setbits = int(comp[-1].replace("X", "0"), 2)
    elif comp[0][:3] == "mem":
        addr = int(comp[0][4:-1])
        temp = int(comp[-1])
        temp &= clearbits
        temp |= setbits
        mem[addr] = temp

print(sum(mem.values()))

mask = None
writes = []
for line in lines:
    comp = line.split()
    if comp[0] == "mask":
        mask = comp[-1][::-1]
    elif comp[0][:3] == "mem":
        addr = int(comp[0][4:-1])
        finaladdr = [0] * 36
        for i in range(36):
            if mask[i] == "1":
                finaladdr[i] = "1"
            elif mask[i] == "X":
                finaladdr[i] = "X"
            elif ((addr >> i) & 1) == 1:
                finaladdr[i] = "1"
            else:
                finaladdr[i] = "0"
        writes.append((finaladdr[::-1], int(comp[-1])))

current = writes[-1][0]
actualwrites = [(current[::], writes[-1][1])]

# print("writes")
# for w in writes:
#     print(''.join(w[0]), w[1])
# print("\nactual")
# for w in actualwrites:
#     print(''.join(w[0]), w[1])
# print()

for w in writes[-2::-1]:
    some = False
    thismask = w[0]
    oldcurrent = current[::]
    count = 0
    for i in range(36):
        if current[i] == "1" and thismask[i] != "1":
            count += 1
            current[i] = "X"
            some = True
            if thismask[i] == "X":
                thismask[i] = "0"
        elif current[i] == "0" and thismask[i] != "0":
            count += 1
            current[i] = "X"
            some = True
            if thismask[i] == "X":
                thismask[i] = "1"
    if some:
        print("current", "".join(oldcurrent))
        print("this   ", "".join(thismask))
        print(count, "\n")
        actualwrites.append((thismask[::], w[1]))

for w in actualwrites:
    print("".join(w[0]), w[1])

print(sum(2 ** addr.count("X") * val for addr, val in actualwrites))

sys.exit()

with open("input") as f:
    first, second = f.readlines()

earliest = int(first)
busses = [int(x) for x in second.split(",") if x != "x"]


def solvea():
    i = earliest
    while True:
        for b in busses:
            if i % b == 0:
                print(b * (i - earliest))
                return
        i += 1


solvea()

busses = [(int(x), n) for n, x in enumerate(second.split(",")) if x != "x"]
# print(busses)
# sys.exit()
for i in range(len(busses)):
    busses[i] = busses[i][0], (busses[i][0] * 2 - busses[i][1]) % busses[i][0]

print(busses)

bus, off = list(zip(*busses))
print(bus, off)


def extended_eucalid(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y


def crt_solve_for_x(off, bus):
    terms = len(off)
    constants = [1] * terms
    product = reduce((lambda x, y: x * y), bus)

    for i in range(terms):
        other_prod = product // bus[i]
        eucalid_result = extended_eucalid(other_prod, bus[i])[0]
        if eucalid_result < 0:
            eucalid_result += bus[i]
        constants[i] = other_prod * eucalid_result * off[i]

    return sum(constants) % product, product


print(crt_solve_for_x([0, 3, 4], [3, 4, 5]))  # should = 39

from math import gcd

for i in bus:
    for j in bus:
        if i != j and gcd(i, j) != 1:
            print("NOPE", i, j)
            sys.exit()  # they're all coprime

print(crt_solve_for_x(off, bus))

sys.exit()

with open("input") as f:
    lines = f.readlines()

d = 0
directions = ["E", "S", "W", "N"]
x = 0
y = 0
for line in lines:
    command, amount = line[0], int(line[1:])
    if command == "F":
        command = directions[d]

    if command == "R":
        d = (d + amount // 90) % 4
    elif command == "L":
        d = (d + 4 - amount // 90) % 4
    elif command == "N":
        y += amount
    elif command == "S":
        y -= amount
    elif command == "E":
        x += amount
    elif command == "W":
        x -= amount

print(abs(x) + abs(y))

x = y = 0
wx = 10
wy = -1
for line in lines:
    command, amount = line[0], int(line[1:])
    if command == "L":
        command = "R"
        amount = 360 - amount
    # print(x, y, "waypoint", wx, wy)
    # print(command, amount)

    if command == "F":
        x += wx * amount
        y += wy * amount
    elif command == "R":
        # print(wx, wy)
        for _ in range(amount // 90):
            (wx, wy) = (-wy, wx)
            # print(wx, wy)
        # print()
    elif command == "N":
        wy -= amount
    elif command == "S":
        wy += amount
    elif command == "E":
        wx += amount
    elif command == "W":
        wx -= amount

print(abs(x) + abs(y))

sys.exit()

with open("input") as f:
    grid = list(map(lambda x: list(x.strip()), f.readlines()))

h = len(grid[0])
w = len(grid)


def neighbors(x, y, g):
    directions = set(itertools.product(range(-1, 2), range(-1, 2)))
    directions.discard((0, 0))
    result = set()
    for (xi, yi) in directions:
        newx = max(min(w - 1, x + xi), 0)
        newy = max(min(h - 1, y + yi), 0)
        result.add((newx, newy))
    result.discard((x, y))
    return sum(g[j][k] == "#" for (j, k) in result)


def extended_neighbors(x, y, g):
    directions = set(itertools.product(range(-1, 2), range(-1, 2)))
    directions.discard((0, 0))
    total = 0
    for (xi, yi) in directions:
        (cx, cy) = (x, y)
        while True:
            cx += xi
            cy += yi
            if cx not in range(0, w) or cy not in range(0, h) or g[cx][cy] == "L":
                break
            if g[cx][cy] == "#":
                total += 1
                break

    return total


def printgrid(g):
    for row in g:
        print("".join(row))
    print("\n")


temp = copy.deepcopy(grid)

while True:
    changed = False
    for x in range(w):
        for y in range(h):
            current = grid[x][y]
            total = extended_neighbors(x, y, grid)
            if current == "L" and total == 0:
                temp[x][y] = "#"
                changed = True
            elif current == "#" and total >= 5:
                temp[x][y] = "L"
                changed = True
    # printgrid(grid)
    if not changed:
        break
    grid = copy.deepcopy(temp)

print(sum(sum(x == "#" for x in row) for row in grid))

sys.exit()

with open("input") as f:
    l = list(map(int, f.readlines()))

dist = 25
target = None
for i in range(dist, len(l)):
    before = l[i - dist : i]
    subs = [l[i] - n for n in before]
    if not any(n in subs for n in before):
        target = l[i]
        break

print(target)

i = 0
j = 0
total = l[0]
while True:
    if total == target:
        r = l[i : j + 1]
        print(max(r) + min(r))
        sys.exit()

    while total < target:
        j += 1
        total += l[j]

    while total > target:
        total -= l[i]
        i += 1


sys.exit()

with open("input") as f:
    l = [0] + sorted(map(int, f.readlines()))
    l += [l[-1] + 3]

diffs = [0, 0, 0]
for i in range(len(l) - 1):
    diff = l[i + 1] - l[i]
    diffs[diff - 1] += 1

print(diffs[0] * diffs[2])

memo = {n: None for n in l}
memo[l[-1]] = 1


def calculate(n):
    if n not in memo:
        return 0
    if not memo[n]:
        memo[n] = calculate(n + 1) + calculate(n + 2) + calculate(n + 3)
    return memo[n]


print(calculate(0))

sys.exit()

with open("input") as f:
    lines = list(enumerate(map(str.split, f.readlines())))

pc = 0
acc = 0
seen = set()

while True:
    if pc in seen:
        print(pc, acc)
        break
    seen.add(pc)
    ins = lines[pc][1][0]
    if ins == "jmp":
        pc += int(lines[pc][1][1])
    else:
        if ins == "acc":
            acc += int(lines[pc][1][1])
        pc += 1


def check(newlines):
    pc = 0
    acc = 0
    seen = set()
    target = len(newlines)

    while pc < target:
        if pc in seen:
            return
        seen.add(pc)
        ins = newlines[pc][1][0]
        if ins == "jmp":
            pc += int(newlines[pc][1][1])
        else:
            if ins == "acc":
                acc += int(newlines[pc][1][1])
            pc += 1

    print(pc, acc)
    sys.exit()


for i in range(len(lines)):
    ins = lines[i][1][0]
    if ins == "nop":
        newlines = copy.deepcopy(lines)
        newlines[i][1][0] = "jmp"
        check(newlines)
    elif ins == "jmp":
        newlines = copy.deepcopy(lines)
        newlines[i][1][0] = "nop"
        check(newlines)

print("didnt find")

sys.exit()

with open("input") as f:
    lines = list(map(str.strip, f.readlines()))

parents = defaultdict(list)
children = defaultdict(list)
for line in lines:
    words = line.split()
    current = " ".join(words[0:2])
    if len(words) == 7:
        children[current] = 1
        continue
    for i in range(4, len(words), 4):
        children[current].append((" ".join(words[i + 1 : i + 3]), int(words[i])))
        parents[(" ".join(words[i + 1 : i + 3]))].append(
            (current, int(words[i])),
        )

contain = set(i[0] for i in parents["shiny gold"])

old_size = len(contain)
new_size = 0

while old_size != new_size:
    new_size = old_size
    to_add = set()
    for name in contain:
        for parent in parents[name]:
            to_add.add(parent[0])
    contain |= to_add
    old_size = len(contain)

print(len(contain))


def count_children(name):
    print(name, "\t", children[name])
    if children[name] == 1:
        return 1
    return 1 + sum(n * count_children(s) for s, n in children[name])


print(count_children("shiny gold") - 1)
sys.exit()

with open("input") as f:
    raw = f.read()
print(sum(len(set(group.replace("\n", ""))) for group in raw.split("\n\n")))
print(sum(len(set.intersection(*map(set, line.split()))) for line in raw.split("\n\n")))

sys.exit()

with open("input") as f:
    stuff = map(str.strip, f.readlines())

ids = set()
for line in stuff:
    fb = line[:7].replace("F", "0").replace("B", "1")
    lr = line[7:].replace("L", "0").replace("R", "1")
    ids.add(int(fb, 2) * 8 + int(lr, 2))

possible = set()
for i in range(1, 127):
    for j in range(8):
        possible.add(i * 8 + j)

print(len(possible), len(ids))
print(max(ids))
print(possible - ids)
sys.exit()

with open("input") as f:
    raw = f.read()
    lines = raw.split("\n\n")
    passports = [dict(elem.split(":") for elem in line.split()) for line in lines]


fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

# def verify(port):
#     return all(f in port for f in fields)


def verify(port):
    if not all(f in port for f in fields):
        return False
    year = port["byr"]
    if not year.isdigit() or not 1920 <= int(year) <= 2002:
        return False
    year = port["iyr"]
    if not year.isdigit() or not 2010 <= int(year) <= 2020:
        return False
    year = port["eyr"]
    if not year.isdigit() or not 2020 <= int(year) <= 2030:
        return False
    height = port["hgt"]
    if height[-2:] == "in":
        n = height[:-2]
        if not n.isdigit() or not 59 <= int(n) <= 76:
            return False
    elif height[-2:] == "cm":
        n = height[:-2]
        if not n.isdigit() or not 150 <= int(n) <= 193:
            return False
    else:
        return False
    hair = port["hcl"]
    if (
        hair[0] != "#"
        or len(hair) != 7
        or not all(c in string.hexdigits for c in hair[1:])
    ):
        return False
    if port["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False
    if len(port["pid"]) != 9 or not port["pid"].isdigit():
        return False
    return True


print(sum((verify(x) for x in passports)))
sys.exit()

dots = [[1 if c == "." else 0 for c in line] for line in lines]


def traverse(right, down):
    x = 0
    y = 0
    count = 0
    while y < len(dots):
        count += not (dots[y][x])
        x += right
        x %= len(dots[0])
        y += down
    return count


# print()
# for row in dots:
#     print("".join(map(str, row)))
# print(dots)
# print()

# print(sum(n.count('#') for n in dots))

# print(traverse(3, 1))
print(
    traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)
)

import sys

sys.exit()
count = 0

for line in lines:
    temp = line.split()
    least, most = map(int, temp[0].split("-"))
    target = temp[1][0]
    print(least, most, target)
    pw = temp[2]
    if (
        pw[least - 1] == target
        and pw[most - 1] != target
        or pw[least - 1] != target
        and pw[most - 1] == target
    ):
        count += 1
    # if least <= temp[2].count(target) <= most:
    #     count += 1

print(count)
