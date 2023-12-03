import re

lines = open("input").read().splitlines()
nums = [[int(i) for i in w if "0" <= i <= "9"] for w in lines]
print(sum(l[0] * 10 + l[-1] for l in nums))
names = "zero one two three four five six seven eight nine".split()
names = {s: i for i, s in enumerate(names)} | {str(i): i for i in range(10)}
digits = lambda s: re.findall(f"(?=({'|'.join(names)}))", s)
print(sum(names[(m := digits(l))[0]] * 10 + names[m[-1]] for l in lines))
