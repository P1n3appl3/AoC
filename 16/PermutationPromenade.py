def dance(data, programs):
    start = 0
    for i in data:
        temp = i[1:].split('/')
        if i[0] == 's':
            start = (start + 16 - int(temp[0])) % 16
        elif i[0] == 'x':
            n = (start + int(temp[0])) % 16
            m = (start + int(temp[1])) % 16
            programs[n], programs[m] = programs[m], programs[n]
        elif i[0] == 'p':
            n = programs.index(ord(temp[0]) - ord('a'))
            m = programs.index(ord(temp[1]) - ord('a'))
            programs[n], programs[m] = programs[m], programs[n]
    return programs[start:] + programs[:start]


moves = open("input.txt").read().strip().split(',')

temp = dance(moves, range(16))

print "Part 1:", ''.join([chr(i + ord('a')) for i in temp])

times = 1000000000
i = 0
first = range(16)
state = range(16)

while i < times:
    state = dance(moves, state)
    i += 1
    if state == first:
        times = times - (times // i) * i
        i = 0

print "Part 2:", ''.join([chr(i + ord('a')) for i in state])
