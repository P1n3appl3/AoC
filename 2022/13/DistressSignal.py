from functools import cmp_to_key


def cmp(a, b):
    typeof = lambda x: repr(type(x))[8]
    match (typeof(a), typeof(b)):
        case ("i", "i"):
            n = a - b
            return n and n // abs(n) or 0
        case ("l", "l"):
            for i in range(min(len(a), len(b))):
                if tmp := cmp(a[i], b[i]):
                    return tmp
            return cmp(len(a), len(b))
        case ("i", "l"):
            return cmp([a], b)
        case ("l", "i"):
            return cmp(a, [b])


lines = list(map(eval, filter(lambda x: x, open("input").read().splitlines())))
pairs = list(zip(lines[::2], lines[1::2]))
print(sum(-(cmp(*p) - 1) // 2 * (i + 1) for i, p in enumerate(pairs)))
all = [[]] + lines + [[[2]], [[6]]]
all.sort(key=cmp_to_key(cmp))
print(all.index([[2]]) * all.index([[6]]))
