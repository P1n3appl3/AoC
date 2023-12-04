nums = lambda l: {int(i) for i in l.split()}
lines = [map(nums, l.split(":")[-1].split("|")) for l in open("input")]
score = lambda n: 1 << n - 1 if n > 0 else 0
matches = [len(winners & yours) for winners, yours in lines]
print(sum(map(score, matches)))

counts = [1] * len(matches)
for i in range(len(matches)):
    for j in range(i + 1, i + 1 + matches[i]):
        counts[j] += counts[i]
print(sum(counts))
