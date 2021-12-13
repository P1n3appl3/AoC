from collections import deque
from functools import reduce as fold

table = {")": 3, "]": 57, "}": 1197, ">": 25137}
othertable = {c: i + 1 for i, c in enumerate(table)}
match = {"(": ")", "{": "}", "<": ">", "[": "]"}
total = 0
scores = []
with open("input") as f:
    for line in f:
        stack = deque()
        skip = False
        for c in line.strip():
            if c in match:
                stack.append(c)
            else:
                off = stack.pop()
                if c != match[off]:
                    total += table[c]
                    skip = True
                    break
        if skip:
            continue
        close = [match[c] for c in stack][::-1]
        scores.append(fold(lambda a, c: 5 * a + othertable[c], close, 0))
print(total)
print(sorted(scores)[len(scores) // 2])
