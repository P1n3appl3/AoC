raw = map(lambda x: x.strip(), open("input.txt"))

from collections import defaultdict
reg = defaultdict(int)
allMaxes = []

for line in raw:
    line = line.split()
    reg[line[0]] += ((line[1] == "inc") * 2 - 1) * int(line[2]) * eval("reg['" + line[4] + "']" + line[5] + line[6])
    allMaxes.append(max(reg.values()))

print "Part 1:", allMaxes[-1]
print "Part 2:", max(allMaxes)
