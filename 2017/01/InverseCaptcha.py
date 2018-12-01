with open("input.txt") as f:
    digits = f.read().strip()

print "Part 1:", sum(int(i[1]) for i in enumerate(digits) if i[1] == digits[i[0] - 1])

print "Part 2:", sum(int(i[1]) for i in enumerate(digits) if i[1] == digits[i[0] - len(digits) / 2])
