from itertools import product


class Program():

    def __init__(self, n, w, c=[]):
        self.name = n
        self.weight = w
        self.children = c

    def updateChildren(self, proglist):
        self.children = [i[1] for i in product(self.children, proglist) if i[0] == i[1].name]

    def getTotalChildren(self):
        return len(self.children) + sum(i.getTotalChildren() for i in self.children)

    def updateTotalWeight(self):
        self.totalWeight = self.weight + sum(i.updateTotalWeight() for i in self.children)
        return self.totalWeight

raw = map(lambda x: x.strip(), open("input.txt"))

programs = []
for line in raw:
    line = line.replace(',', ' ').split()
    programs.append(Program(line[0], int(line[1][1:-1]), line[3:]))

for p in programs:
    p.updateChildren(programs)

programs.sort(key=lambda p: p.getTotalChildren())

print "Part 1:", programs[-1].name

programs[-1].updateTotalWeight()


def balance(p, needs=0):
    if not p.children:
        return
    if len(set([i.totalWeight for i in p.children])) == 1:
        return

    p.children.sort(key=lambda i: i.totalWeight)
    if not needs:
        needs = p.children[-1].totalWeight - p.children[0].totalWeight
        if p.children[0].totalWeight == p.children[1].totalWeight:
            needs = -needs

    kidsresults = [balance(i, needs) for i in p.children]
    if any(kidsresults):
        return [i for i in kidsresults if i][0]

    if needs > 0:
        return p.children[0].weight + needs
    return p.children[-1].weight + needs

print "Part 2:", balance(programs[-1])
