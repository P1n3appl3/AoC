skip = 344
pos = 0
buff = []

for i in range(2018):
    buff.insert(pos, i)
    pos = (skip + pos) % len(buff) + 1

print "Part 1:", buff[buff.index(2017) + 1]

pos = 0
current = None
for i in range(50000000):
    if pos == 1:
        current = i
    pos = (skip + pos) % (i+1) + 1

print "Part 2:", current
