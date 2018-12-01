particles = [[map(int, n[3:-1].split(','))
              for n in s.strip().split(', ')][::-1]
             for s in open("input.txt").readlines()]

print "Part 1:", min(
    enumerate(map(sum, [map(abs, n) for n in i]) for i in particles),
    key=lambda n: n[1])[0]

for _ in range(50):
    col = []
    new = []
    for p in particles:
        if p[2] in col:
            continue
        for n in new:
            if p[2] == n[2]:
                col.append(p[2])
                continue
        new.append(p)
    particles = [n for n in new if not n[2] in col]
    for p in particles:
        p[1] = [sum(x) for x in zip(p[0], p[1])]
        p[2] = [sum(x) for x in zip(p[1], p[2])]

print "Part 2:", len(particles)
