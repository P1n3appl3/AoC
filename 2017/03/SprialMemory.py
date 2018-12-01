from math import sqrt

n = 347991

ring = 0
while 4 * (ring**2 + ring) < n:
    ring += 1
ring -= 1
temp = n - 4 * (ring**2 + ring) - 1

print "Part 1:", ring * 2 + sum(([1] + [-1] * ring + ([1] * (ring + 1) + [-1] * (ring + 1)) * 3 + [1] * (ring + 1))[:temp])

import numpy as np

rotate = lambda x: np.asarray(np.matrix([x[0], x[1]]) * np.matrix([[0, 1], [-1, 0]]))[0]

board = np.zeros((300, 300), np.int32)
pos = np.array([150, 150])
direction = np.array([1, 0])
neighbors = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
board[pos[0], pos[1]] = 1
pos += direction

for i in range(n):
    board[pos[0], pos[1]] = sum(board[pos[0] + i[0], pos[1] + i[1]] for i in neighbors)
    if board[pos[0], pos[1]] > n:
        print "Part 2:", board[pos[0], pos[1]]
        break
    temp = rotate(direction)
    if not board[pos[0] + temp[0], pos[1] + temp[1]]:
        direction = rotate(direction)
    pos += direction
