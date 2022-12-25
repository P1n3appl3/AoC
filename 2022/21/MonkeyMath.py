import operator as op

tree = {}
operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.floordiv}
inv_ops = {"+": op.sub, "-": op.add, "*": op.floordiv, "/": op.mul}
parent = {}
for line in open("input"):
    name = line[:4]
    if (rest := line[6:-1]).isnumeric():
        tree[name] = int(rest)
    else:
        l, r = rest[:4], rest[7:11]
        parent[l] = parent[r] = name
        tree[name] = (rest[5], l, r)

# # dot
# print("digraph G {")
# for k, v in waiting.items():
#     print(k, "->", f"{{{', '.join(v[1:])}}}")
# print("}")


def solve(n):
    if type(tree[n]) is int:
        return tree[n]
    op, l, r = tree[n]
    return operators[op](solve(l), solve(r))


print(solve("root"))


def rev(cur):
    child = cur
    cur = parent[child]
    op, l, r = tree[cur]
    if cur == "root":
        # print(cur, l, "=", r, "  :  ", solve(r if l == child else l))
        return solve(r if l == child else l)
    par = rev(cur)
    # print(cur, "=", l, op, r, end="  :  ")
    if l == child:
        # print(par, op, solve(r))
        return inv_ops[op](par, solve(r))
    else:
        # print("-" if op == "-" else "" + str(par), op, solve(l))
        return inv_ops[op](((op != "-") * 2 - 1) * par, solve(l))


print(rev("humn"))
