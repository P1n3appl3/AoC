print("digraph{")
with open("test") as f:
    f.readline()
    f.readline()
    for line in f:
        l, r = line.split("->")
        r = r.strip()
        a, b = l.strip()
        print(a + b, "->", a + r)
        print(a + b, "->", r + b)
print("}")
