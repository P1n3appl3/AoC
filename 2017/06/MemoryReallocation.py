with open("input.txt") as f:
    banks = map(int, f.read().split())

archive = []
while True:
    archive.append(banks[:])
    biggest = 0
    choose = 0
    for i in range(len(banks)):
        if banks[i] > biggest:
            biggest = banks[i]
            choose = i
    temp = banks[choose]
    banks[choose] = 0
    i = choose + 1
    while temp > 0:
        banks[i % len(banks)] += 1
        i += 1
        temp -= 1
    if banks in archive:
        break

print "Part 1:", len(archive)

print "Part 2:", len(archive) - archive.index(banks)
