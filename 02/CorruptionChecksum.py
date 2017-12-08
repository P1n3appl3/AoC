with open("input.txt") as f:
    sheet = [map(int, i.split()) for i in f.readlines()]

print "Part 1:", sum(max(i) - min(i) for i in sheet)

from itertools import permutations

print "Part 2:", sum(sum(i[0] / i[1] for i in permutations(j, 2) if i[0] % i[1] == 0) for j in sheet)
