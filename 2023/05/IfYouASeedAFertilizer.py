from functools import reduce

sections = open("input").read().split("\n\n")
seeds = [int(s) for s in sections[0].split()[1:]]
maps = [[list(map(int, s.split())) for s in l.splitlines()[1:]] for l in sections[1:]]
maps = [sorted([(src, dest, len) for dest, src, len in stage]) for stage in maps]
trymap = lambda n, src, dest, l: dest - src + n if n in range(src, src + l) else None
some = lambda l: [x for x in l if x is not None]
step = lambda cur, stage: [(some([trymap(n, *m) for m in stage]) + [n])[0] for n in cur]

print(min(reduce(lambda cur, stage: step(cur, stage), maps, seeds)))

seeds = [range(a, a + b) for a, b in zip(seeds[::2], seeds[1::2])]
seeds.sort(key=lambda r: r.start)
for stage in maps:
    s = m = 0
    seed = seeds[s]
    result = []
    while seed:
        if m >= len(stage):
            result.append(seed)
            for i in range(s + 1, len(seeds)):
                result.append(seeds[i])
            break
        src, dest, l = stage[m]
        if seed.stop < src:
            result.append(seed)
            s += 1
            seed = seeds[s] if s < len(seeds) else None
        elif src + l < seed.start:
            m += 1
        elif (start := trymap(seed.start, src, dest, l)) is not None:
            if (stop := trymap(seed.stop, src, dest, l)) is not None:
                result.append(range(start, stop))
                s += 1
                seed = seeds[s] if s < len(seeds) else None
            else:
                stop = src + l
                result.append(range(start, dest + l))
                m += 1
                seed = range(src + l, seed.stop)
        else:
            result.append(range(seed.start, src))
            result.append(range(dest, dest + seed.stop - src))
            s += 1
            seed = seeds[s] if s < len(seeds) else None
    seeds = sorted(result, key=lambda r: r.start)

print(seeds[0].start)
