with open("input.txt") as f:
    raw = f.read().strip()
    inputs = map(int, raw.split(','))

length = 256
knot = range(length)
skip = 0
current = 0

for i in inputs:
    for j in range(i // 2):
        front = (current + j) % length
        back = (current + i - j - 1) % length
        knot[front], knot[back] = knot[back], knot[front]
    current += i + skip
    skip += 1

print "Part 1:", knot[0] * knot[1]

knot = range(length)
skip = 0
current = 0
for n in range(64):
    for i in map(ord, raw) + [17, 31, 73, 47, 23]:
        for j in range(i // 2):
            front = (current + j) % length
            back = (current + i - j - 1) % length
            knot[front], knot[back] = knot[back], knot[front]
        current += i + skip
        skip += 1

dense = [reduce(lambda x, y: x ^ y, knot[i * 16:(i + 1) * 16]) for i in range(16)]

print "Part 2:", ''.join(hex(i)[2:].zfill(2) for i in dense)
