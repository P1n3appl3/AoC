from collections import deque
from operator import or_, and_, xor


with open("input") as f:
    initial, allgates = f.read().split("\n\n")

values = {name: int(val) for name, val in [s.split(":") for s in initial.splitlines()]}
gates = deque()
for g in allgates.splitlines():
    l, op, r, _, out = g.split()
    gates.append((l, r, {"AND": and_, "OR": or_, "XOR": xor}[op], out))
original = gates.copy()

while len(gates) > 0:
    if not any(g[3].startswith("z") for g in gates):
        break
    (l, r, op, out) = cur = gates.popleft()
    if l in values and r in values:
        values[out] = op(values[l], values[r])
    else:
        gates.append(cur)

extract = lambda l: ((int(k[1:]), v) for k, v in values.items() if k.startswith(l))
num = lambda name: sum([b * 2**i for i, b in sorted(extract(name))])

print(num("z"))

print(f"{num("z"):046b}")
# x, y = num("x"), num("y")
# print(f"{x+y:046b}")
# print()
# print(f"{x:046b}")
# print(f"{y:046b}")

r"""
how to add stuff:

z0 = x0 ^ y0
c0 = x0 & y0

e1 = x1 ^ y1
z1 = e1 ^ c0
t1 = e1 & c0
a1 = x1 & y1
c1 = a1 | t1

e2 = x2 ^ y2
z2 = e2 ^ c1
t2 = e2 & c1
a2 = x2 & y2
c2 = a2 | t2

...

e(xor)  = x ^ y
z(um)   = e ^ c⁻¹
t(mp)   = e & c⁻¹
a(nd)   = x & y
c(arry) = a | t     (except on last? or last carry is z⁺¹)

so gate counts for input with b bits should be:
 OR: b
XOR: 2b + 1
AND: 2b + 1

counts for my input:
 OR: 44
AND: 89
XOR: 89

that means no extra gates which makes things way easier!
i was so worried we'd have to do disjunctive normal form and
minimization and SAT solving 😅

wait a sec... if this is really just gonna be a bunch of term renaming, how
far can i get with vim?
put x's on left: :%s/y\(\d\d\) \(\S*\) x../x\1 \2 y\1
sort by operation: :sort /.*\%3v/

add some newlines between the e/z xors and the a/t ands so you can see the
5 groups of gates clearly.

to rename xors: 0mal"ay2l$b"byw:%s/b/ea
'aj
                                       ⬆
do the same for other letters by swapping this char

now lets compute t, start by flipping all the "e\d\d"'s to the left side
similarly to how we did x's at the start: %s/\(...\) \([A-Z]*\) \(e..\)/\3 \2 \1

wait a sec, one of the ANDs doesn't have an e term... hopefully that means
this is the first swapped wire. go back through the original input file to
find their names

alright back to computing temps. because we have mismatched numbers on the
lhs and rhs, it's easiest to add a line to use as a loop variable of sorts
at the top of the file, then we can use marks, gg, and ` to create a macro
that goes to the top of the file, increments and yanks it, and then goes
back to the mark, down a line and does a replacement similar to the xor
renaming one.

... actually scratch that, a simpler way would be to handle the ORs first
since the numbers do line up there. also i think i see more mismatched wires?

i continued to bumbled through like this and found the 4 pairs. I think
I could write code to automate the renaming process, the annoying part
would be accounting for the kinds of swaps (a,t,z,e,c pick 2). I don't
feel like doing that especially because this approach falls over in the
face of any extraneous gates, and maybe doesn't handle swaps across
different bits?
"""
