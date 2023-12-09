from collections import Counter

lines = map(str.split, open("input").readlines())
values = {c: i for i, c in enumerate("23456789TJQKA")}
hands = [([values[c] for c in a], int(b)) for a, b in lines]


def rank(hand, jokers=False):
    if jokers:
        hand = list(filter(values["J"].__ne__, hand))
    counts = sorted(Counter(hand).values()) or [0]
    counts[-1] += 5 - len(hand)
    return counts[::-1]


hands.sort(key=lambda h: (rank(h[0]), h[0]))
print(sum(i * bid for i, (_, bid) in enumerate(hands, start=1)))
replacej = lambda h: [-1 if i == values["J"] else i for i in h]
hands.sort(key=lambda h: (rank(h[0], True), replacej(h[0])))
print(sum(i * bid for i, (_, bid) in enumerate(hands, start=1)))
