phrases = map(lambda x: x.split(), open("input.txt"))

print "Part 1:", [len(i) == len(set(i)) for i in phrases].count(True)

for i in range(len(phrases)):
    phrases[i] = [''.join(sorted(j)) for j in phrases[i]]

print "Part 2:", [len(i) == len(set(i)) for i in phrases].count(True)
