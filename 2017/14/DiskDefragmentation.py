raw = "hwlqcszp"
length = 256
board = []
for q in range(128):
    knot = range(length)
    skip = 0
    current = 0
    for n in range(64):
        for i in map(ord, raw + '-' + str(q)) + [17, 31, 73, 47, 23]:
            for j in range(i // 2):
                front = (current + j) % length
                back = (current + i - j - 1) % length
                knot[front], knot[back] = knot[back], knot[front]
            current += i + skip
            skip += 1
    board.append(reduce(lambda x, y: x + y, [map(int, bin(i)[2:].zfill(8)) for i in [reduce(lambda x, y: x ^ y, knot[i * 16:(i + 1) * 16]) for i in range(16)]]))

print "Part 1:", sum(i.count(1) for i in board)


def explore(x, y):
    board[x][y] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (j == 0 or i == 0) and 0 <= x + i < 128 and 0 <= y + j < 128 and board[x + i][y + j]:
                explore(x + i, y + j)

total = 0
for i in range(128):
    for j in range(128):
        if board[i][j]:
            total += 1
            explore(i, j)

print "Part 2:", total
