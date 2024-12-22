from operator import xor

with open("input") as f:
    numbers = [int(l) for l in f.readlines()]


def evolve(n, steps=2000):
    mix = xor
    prune = lambda n: n % 16777216
    res = [n]
    for _ in range(steps):
        n = prune(mix(n * 64, n))
        n = prune(mix(n // 32, n))
        n = prune(mix(n * 2048, n))
        res.append(n)
    return res


buyers = [evolve(n) for n in numbers]
print(sum(prices[-1] for prices in buyers))
buyers = [[p % 10 for p in prices] for prices in buyers]
diffs = [
    [prices[i + 1] - prices[i] for i in range(len(prices) - 1)] for prices in buyers
]
best = []
for b, d in zip(buyers, diffs):
    seen = {}
    for i in range(len(d) - 3):
        seq, score = tuple(d[i : i + 4]), b[i + 4]
        if seq not in seen:
            seen[seq] = score
    best.append(seen)

seqs = {k for keys in best for k in keys}
ans = 0
for s in seqs:
    ans = max(ans, sum(b.get(s) or 0 for b in best))
print(ans)
