def run(a, b, c, instructions):
    out = []

    def combo(n):
        match n:
            case n if n <= 3:
                return n
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                exit("unsupported")

    ip = 0
    while True:
        if ip > (len(instructions) - 2):
            break
        i, n = instructions[ip : ip + 2]
        # print(ip, i, n)
        ip += 2
        match i:
            case 0:
                a >>= combo(n)
            case 1:
                b ^= n
            case 2:
                b = combo(n) % 8
            case 3:
                if a != 0:
                    ip = n
            case 4:
                b ^= c
            case 5:
                out.append(combo(n) % 8)
            case 6:
                b = a >> combo(n)
            case 7:
                c = a >> combo(n)
    return out


def dot(instructions):
    nodes = []
    edges = []

    def combo(n):
        match n:
            case n if n <= 3:
                return n
            case 4:
                return "a"
            case 5:
                return "b"
            case 6:
                return "c"
            case _:
                return "illegal"

    for ip in range(len(instructions) - 1):
        i, n = instructions[ip : ip + 2]
        if ip >= 2:
            edges.append((ip - 2, ip))
        c = combo(n)
        match i:
            case 0:
                temp = (2**c) if type(c) is int else f"2^{c}"
                # nodes.append(f"ADV {temp}")
                nodes.append(f"a>>={c}")
            case 1:
                # nodes.append(f"BXL {n}")
                nodes.append(f"b^={n}")
            case 2:
                temp = (c % 8) if type(c) is int else f"{c}%8"
                # nodes.append(f"BST {temp}")
                nodes.append(f"b={temp}")
            case 3:
                nodes.append(f"JNZ {n}")
                edges.append((ip, n))
                # TODO: don't make node here
            case 4:
                # nodes.append("BXC")
                nodes.append("b^=c")
            case 5:
                temp = (c % 8) if type(c) is int else f"{c}%8"
                nodes.append(f"OUT {temp}")
            case 6:
                # temp = (2**c) if type(c) is int else f"2^{c}"
                # nodes.append(f"BDV {temp}")
                nodes.append(f"b=a>>{c}")
            case 7:
                # temp = (2**c) if type(c) is int else f"2^{c}"
                # nodes.append(f"CDV {temp}")
                nodes.append(f"c=a>>{c}")

    print("digraph {")
    for name, label in enumerate(nodes):
        print(f'i{name} [label="{label}"]')
    for l, r in edges:
        print(f"i{l} -> i{r}")
    print(f"i{len(instructions)-2} -> END")
    print(f"i{len(instructions)-3} -> END")
    print("START -> i0")
    print("}")
    exit()


with open("input") as f:
    raw = f.read()

regs, program = raw.split("\n\n")
(a, b, c) = [int(s.split()[-1]) for s in regs.splitlines()]
instructions = [int(i) for i in program.split()[-1].split(",")]
ans = ",".join((map(str, run(a, b, c, instructions))))
print(ans)

# dot(instructions)


def p2(cur, instructions):
    out = instructions[-1]
    # print((16 - len(instructions)) * " ", cur, out)
    for a in range(8):
        b = a ^ 0b101
        c = ((cur | a) >> b) & 0b111
        temp = b ^ c ^ 0b110
        # print((16 - len(instructions)) * " ", f"{a:0b} {temp:0b}")
        if temp == out:
            # print(f"{out}: {cur|a:048b}")
            if len(instructions) == 1:
                return cur | a
            if ans := p2((cur | a) << 3, instructions[:-1]):
                return ans
    return None


ans = p2(0, instructions)
# print(run(ans, 0, 0, instructions))
# print(instructions)
print(ans)
