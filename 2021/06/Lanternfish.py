start = list(map(int, open("input").read().split(",")))
current = [1] * 8 + [0] * 293
new = [1] + [0] * 299
def size(n):
    if not current[n]:
        current[n] = size(n-1) + new[n-9] + new[n-7]
        new[n] = new[n-9] + new[n-7]
    return current[n]

def solve(l, n):
    return sum((size(n + 2 + 6-x) for x in l))

print(solve(start, 80))
print(solve(start, 256))

tick = lambda l: [n-1 if n > 0 else 6 for n in l] + [8] * l.count(0)
# a = start[:]
# for i in range(80):
    # a = tick(a)
    # print("[", ' '.join(map(str,a)), "]")
    # print(i, len(a), size(i+1))
    # size(i+3)
    # print(a.count(8), new[i+3])
# print(len(a))
