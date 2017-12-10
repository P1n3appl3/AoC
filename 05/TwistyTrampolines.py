with open("input.txt") as f:
    offsets = map(int, f.readlines())

preserved = offsets[:]
from datetime import datetime

for i in range(1, 3):
    offsets = preserved[:]
    start = datetime.now()
    place = 0
    steps = 0
    while 0 <= place < len(offsets):
        temp = place + offsets[place]
        offsets[place] += 1 - 2 * (offsets[place] > 2) * (i == 2)
        place = temp
        steps += 1

    end = datetime.now()
    print "Part " + str(i) + ":", steps, "\t\tTime:", (end - start).total_seconds()
