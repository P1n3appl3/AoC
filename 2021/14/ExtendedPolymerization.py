rules = {}
counts = {}
letters = {}

with open("input") as f:
    start = f.readline().strip()
    f.readline()
    polymers = [tuple(map(str.strip, line.split("->"))) for line in f]
    for pair, to in polymers:
        letters[to] = 0
        counts[pair] = 0
        rules[pair] = to

for l in start:
    letters[l] += 1
for i in range(len(start) - 1):
    counts[start[i : i + 2]] += 1


def apply(counts):
    new = counts.copy()
    for pair in rules:
        l, r = pair
        m = rules[pair]
        letters[m] += counts[pair]
        new[pair] -= counts[pair]
        new[l + m] += counts[pair]
        new[m + r] += counts[pair]
    return new


ans = lambda x: max(x) - min(x)

for _ in range(10):
    counts = apply(counts)

print(ans(letters.values()))

for _ in range(30):
    counts = apply(counts)

print(ans(letters.values()))
