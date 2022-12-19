from operator import add, sub

tupadd = lambda a, b: tuple(map(add, a, b))
dirs = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
rope = 10 * [(0, 0)]
part1 = set()
part2 = set()

for line in open("input"):
    dir, times = line.split()
    for _ in range(int(times)):
        rope[0] = tupadd(rope[0], dirs[dir])
        for i in range(1, 10):
            dist = tuple(map(sub, rope[i - 1], rope[i]))
            norm = lambda n: abs(n) and n // abs(n) or 0
            if any(map(lambda x: x not in (-1, 0, 1), dist)):
                rope[i] = tupadd(rope[i], map(norm, dist))
        part1.add(rope[1])
        part2.add(rope[-1])

print(len(part1))
print(len(part2))

# for y in range(5):
#     print("".join("#" if (x, 4 - y) in part1 else "." for x in range(5)))
