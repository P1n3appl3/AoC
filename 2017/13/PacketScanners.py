depths = {}
for i in open("input.txt"):
    temp = i.split(":")
    depths[int(temp[0])] = int(temp[1])


def travel(n, stop=False):
    severity = 0
    for i in depths:
        if not (i + n) % ((depths[i] - 1) * 2):
            if stop:
                return True
            severity += depths[i] * i
    return severity

print "Part 1:", travel(0)

delay = 0
while True:
    if not travel(delay, True):
        print "Part 2:", delay
        break
    delay += 1
