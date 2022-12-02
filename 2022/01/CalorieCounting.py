with open("input") as f:
    elves = f.read().split("\n\n")

elves = sorted(sum(int(x) for x in elf.split()) for elf in elves)
print(elves[-1])
print(sum(elves[-3:]))
