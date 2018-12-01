import os

instructions = map(str.split, open("input.txt").readlines())

reg = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

freq = 0
line = 0
firstTime = True
soundEnabled = True


def fset(x, y):
    reg[x] = int(y)


def fadd(x, y):
    reg[x] += int(y)


def fmul(x, y):
    reg[x] *= int(y)


def fmod(x, y):
    reg[x] %= int(y)


def fjgz(x, y):
    global line
    if int(x) > 0:
        line += int(y) - 1


def frcv(x, y):
    global firstTime
    if reg[x] != 0 and firstTime:
        firstTime = False
        return True


def fsnd(x, y):
    global freq, soundEnabled
    freq = int(x)
    if soundEnabled:
        os.system("beep -f" + str(x))


functions = {
    "set": fset,
    "add": fadd,
    "mul": fmul,
    "mod": fmod,
    "jgz": fjgz,
    "rcv": frcv,
    "snd": fsnd
}

while line < len(instructions):
    current = instructions[line]
    arg1 = current[1]
    if 'a' <= arg1 <= 'z' and current[0] in ("snd", "jgz"):
        arg1 = reg[arg1]
    arg2 = None
    if len(current) > 2:
        arg2 = current[2]
        if 'a' <= arg2 <= 'z':
            arg2 = reg[arg2]
    if functions[current[0]](arg1, arg2):
        break
    line += 1

print "Part 1:", freq

waiting = [False, False]
reg = {i: 0 for i in reg}
altreg = dict(reg)
altreg['p'] = 1
line = 0
altline = 0
from collections import deque
queue = [deque(), deque()]
prog1sent = 0


def fsend(x, y):
    global prog, prog1sent
    queue[not prog].append(int(x))
    prog1sent += (prog == 1)


def freceive(x, y):
    global prog
    waiting[prog] = x


functions["snd"] = fsend
functions["rcv"] = freceive

while False in waiting or any(len(i) > 0 for i in queue):
    for prog in range(2):
        if waiting[prog]:
            if len(queue[prog]):
                reg[waiting[prog]] = queue[prog].popleft()
                waiting[prog] = False
            else:
                reg, altreg = altreg, reg
                line, altline = altline, line
                continue

        current = instructions[line]
        arg1 = current[1]
        if 'a' <= arg1 <= 'z' and current[0] in ("snd", "jgz"):
            arg1 = reg[arg1]
        arg2 = None
        if len(current) > 2:
            arg2 = current[2]
            if 'a' <= arg2 <= 'z':
                arg2 = reg[arg2]
        functions[current[0]](arg1, arg2)
        line += 1
        line, altline = altline, line
        reg, altreg = altreg, reg

print "Part 2:", prog1sent
