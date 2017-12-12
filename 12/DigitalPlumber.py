def follow(n):
    visited = set([n])
    examine = [n]
    while len(examine) > 0:
        for i in pipes[examine.pop()]:
            if i not in visited:
                visited.add(i)
                examine.append(i)
    return visited

with open("input.txt") as f:
    pipes = map(lambda x: map(int, x.replace(',', ' ').strip().split()[2:]), f.readlines())

print "Part 1:", len(follow(0))

pids = set(range(len(pipes)))
groups = 0
while len(pids) > 0:
    groups += 1
    pids -= follow(pids.pop())

print "Part 2:", groups
