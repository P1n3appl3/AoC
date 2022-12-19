from dataclasses import dataclass
from collections import deque
from copy import deepcopy
from math import lcm


@dataclass
class M:
    items: deque[int]; op: str; test: int; yes: int; no: int; count: int=0  # fmt: skip


def round(monkeys, max):
    for m in monkeys:
        for _ in range(len(m.items)):
            old = m.items.popleft()
            new = eval(m.op)
            new = new % max if max else new // 3
            monkeys[m.yes if not new % m.test else m.no].items.append(new)
            m.count += 1


def solve(monkeys, times, divide):
    max = 0 if divide else lcm(*(m.test for m in monkeys))
    for i in range(times):
        round(monkeys, max)
    counts = sorted((m.count for m in monkeys), reverse=True)
    return counts[0] * counts[1]


lines = [s.split(":")[-1].strip() for s in open("input").readlines()]
monkeys = [
    M(
        deque(map(int, c[1].split(","))),
        compile(c[2].split("= ")[-1], "", "eval"),
        *(int(x.split()[-1]) for x in c[3:6]),
    )
    for c in [lines[i : i + 7] for i in range(0, len(lines), 7)]
]
print(solve(deepcopy(monkeys), 20, True))
print(solve(deepcopy(monkeys), 10_000, False))
