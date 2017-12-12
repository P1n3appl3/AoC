with open("input.txt") as f:
    raw = f.read().strip().split(',')

directions = {'n': (1, -1, 0),
              'nw': (1, 0, -1),
              'sw': (0, 1, -1),
              's': (-1, 1,  0),
              'se': (-1,  0, 1),
              'ne': (0, -1, 1)}

total = [0, 0, 0]
distances = []

for i in raw:
    total = map(sum,zip(total,directions[i]))
    distances.append(abs(max(total)))

print "Part 1:", distances[-1]
print "Part 2:", max(distances)
