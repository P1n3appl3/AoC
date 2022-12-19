import copy

listings = []
size = 0
dirs = 0
for line in open("input"):
    if line.startswith("$"):
        if dirs or size:
            listings.append([dirs, size])
            dirs = size = 0
    elif line.startswith("d"):
        dirs += 1
    else:
        size += int(line.split()[0])
listings.append([0, size])

allsizes = []
ans = 0
i = len(listings) - 1
while i >= 0:
    cur = listings[i]
    while cur[0] > 0:
        cur[1] += listings[i+1][1]
        del listings[i+1]
        cur[0] -= 1

    allsizes.append(cur[1])
    if cur[1] <= 100_000:
        ans += cur[1]
    i -= 1

print(ans)

diff = allsizes[-1] - 40_000_000
print(min(filter(lambda n: n>=diff, allsizes)))

