with open("input") as f:
    raw = f.read()

towels, patterns = raw.split("\n\n")
towels = [s.strip() for s in towels.split(",")]
patterns = list(patterns.splitlines())


def solve(cur, path, memo, p2=False):
    if cur in memo:
        return memo[cur]
    if not cur:
        return 1
    total = 0
    for t in towels:
        if cur.startswith(t):
            memo[cur] = solve(cur.removeprefix(t), path + [t], memo, p2)
            if p2:
                total += memo[cur]
            else:
                total |= memo[cur]
    memo[cur] = total
    return total


print(sum(solve(p, [], {}) for p in patterns))
print(sum(solve(p, [], {}, True) for p in patterns))
