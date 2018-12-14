class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


def show(current):
    while current.data != 0:
        current = current.next
    temp = [current.data]
    current = current.next
    while current.data != 0:
        temp.append(current.data)
        current = current.next
    print(temp)


def simulate(players, last):
    scores = [0] * players
    current = Node(0)
    current.next = current
    current.prev = current
    player = 0
    for i in range(1, last + 1):
        if i % 23 == 0:
            for _ in range(7):
                current = current.prev
            scores[player] += i + current.data
            prev = current.prev
            current = current.next
            prev.next = current
            current.prev = prev
        else:
            current = current.next
            temp = current.next
            current.next = Node(i)
            current.next.prev = current
            current = current.next
            current.next = temp
            temp.prev = current
        player = (player + 1) % len(scores)
    return max(scores)


with open("input.txt") as f:
    stuff = f.read().strip().split()

players = int(stuff[0])
last = int(stuff[6])

print("max score:", simulate(players, last))
print("max score (x100):", simulate(players, last * 100))
