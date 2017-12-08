with open("input.txt") as f:
    offsets = map(int, f.readlines())

preserved = offsets[::]

from datetime import datetime
start = datetime.now()
place = 0
steps = 0
while 0 <= place < len(offsets):
    offsets[place] += 1
    place += offsets[place] - 1
    steps += 1

end = datetime.now()
print "Part 1:", steps, "\t\tTime:", (end-start).total_seconds()
offsets = preserved

start = datetime.now()
place = 0
steps = 0
while 0 <= place < len(offsets):
    temp = place + offsets[place]
    offsets[place] += 1 - 2 * (offsets[place] > 2)
    place = temp
    steps += 1

end = datetime.now()
print "Part 2:", steps, "\tTime:", (end-start).total_seconds()
