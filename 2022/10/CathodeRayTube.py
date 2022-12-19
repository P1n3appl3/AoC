from itertools import accumulate, starmap
from operator import mul

steps = [0, 1]
for line in open("input"):
    steps += [0] if line.startswith("n") else [0, int(line.split()[-1])]
cycles = list(accumulate(steps))
print(sum(starmap(mul, list(enumerate(cycles))[20::40])))
for i in range(1, len(steps) - 1):
    pos = (i - 1) % 40
    if not pos:
        print()
    print("#" if abs(pos - cycles[i]) < 2 else ".", end="")
print()
