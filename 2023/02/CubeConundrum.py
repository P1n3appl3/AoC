import re
from collections import Counter
from functools import reduce
from operator import or_, mul

turn = lambda t: {color: int(num) for num, color in re.findall(r"(\d+) (r|g|b)", t)}
games = [[Counter(turn(t)) for t in l.split(";")] for l in open("input")]
min, max = Counter({"r": 0, "g": 0, "b": 0}), Counter({"r": 12, "g": 13, "b": 14})
print(sum(i for i, g in enumerate(games, start=1) if max | reduce(or_, g) == max))
print(sum(reduce(mul, reduce(or_, g).values()) for g in games))
