board = open("input.txt").readlines()
board.insert(0, ' ' * len(board[0]))
board.append(' ' * len(board[0]))
board = [' ' + i + ' ' for i in board]

y = 1
x = board[1].index('|')
ydir = 1
xdir = 0
steps = 0

print "Part 1: ",

while board[y][x] != ' ':
    #print "pos:", x, y, "\t", board[y][x], "\tdir:", xdir, ydir
    steps += 1
    current = board[y][x]
    if current.isalpha():
        print '\b' + current,
    if not current in '|-':
        temp = '|'
        if xdir == 0:
            temp = '-'
            for tempdir in range(-1, 2, 2):
                if board[y][x + tempdir] == temp:
                    ydir = 0
                    xdir = tempdir
        else:
            for tempdir in range(-1, 2, 2):
                if board[y + tempdir][x] == temp:
                    xdir = 0
                    ydir = tempdir
    x += xdir
    y += ydir

print "\nPart 2:", steps
