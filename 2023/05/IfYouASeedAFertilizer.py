from itertools import count

sections = open("input").read().split("\n\n")
seeds = cur = [int(s) for s in sections[0].split()[1:]]
maps = [[list(map(int, s.split())) for s in l.splitlines()[1:]] for l in sections[1:]]


def trans(n, maps, reverse=False):
    for dest, src, l in maps:
        if reverse:
            src, dest = dest, src
        if n in range(src, src + l):
            return dest + (n - src)
    return n


for stage in maps:
    cur = [trans(n, stage) for n in cur]

print(min(cur))

seeds = [range(a, a + b) for a, b in zip(seeds[::2], seeds[1::2])]
for i in count():
    if i % 100000 == 0:
        print(".", end="", flush=True)
    cur = i
    for stage in maps[::-1]:
        cur = trans(cur, stage, True)
    if any(cur in s for s in seeds):
        print(f"\n{i}")
        break
