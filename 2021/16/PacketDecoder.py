from functools import reduce as fold
from operator import mul

def tobits(s):
    temp = bin(int(s, 16))[2:]
    dif = len(temp) % 4
    if dif != 0:
        temp = "0" * (4 - dif) + temp
    return temp


bits = tobits(open("input").read())

def parse(b):
    version = int(b[:3], 2)
    type = int(b[3:6], 2)
    # print("parsing:", version, type, len(b))
    # print(b)
    if type == 4:
        pos = 6
        num = ""
        while True:
            current = b[pos : pos + 5]
            num += current[1:]
            pos += 5
            if current[0] == "0":
                break
        # print("val:", int(num, 2))
        return (version, int(num, 2), pos)
    msgs = []
    if b[6] == "1":
        pos = 18
        subs = int(b[7:pos], 2)
        # print("sub messages:", subs)
        for _ in range(subs):
            v, n, p = parse(b[pos:])
            msgs.append(n)
            version += v
            pos += p
    else:
        pos = 22
        size = int(b[7:22], 2)
        while pos - 22 < size:
            v, n, p = parse(b[pos:])
            msgs.append(n)
            version += v
            pos += p
    match type:
        case 0:
            n = sum(msgs)
        case 1:
            n = fold(mul, msgs)
        case 2:
            n = min(msgs)
        case 3:
            n = max(msgs)
        case 5:
            n = msgs[0] > msgs[1]
        case 6:
            n = msgs[0] < msgs[1]
        case 7:
            n = msgs[0] == msgs[1]
        case other:
            n = 0
            print(f"Error: unknown type ({other})")
    return (version, int(n), pos)


print(parse(bits)[0])
print(parse(bits)[1])
