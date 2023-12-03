from z3 import *

total = 0
digits_list = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
digits = {d: i for i, d in enumerate(digits_list)}


def transform(digits):
    grid = [[int((chr(ord("a") + i)) in d) for i in range(7)] for d in digits]
    return grid
    # return [int("".join(map(str, row)), 2) for row in grid]


grid = transform(digits)
print(grid)

with open("input") as f:
    for line in f:
        line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        signal, output = map(str.split, line.split("|"))
        total += sum(map(lambda n: len(n) in [2, 3, 4, 7], output))

        signal = transform(signal)
        print(signal)
        S = [Int("S_" + chr(ord("a") + i)) for i in range(7)]
        range_c = [And(0 <= S[i], S[i] <= 6) for i in range(7)]
        unique_c = [Distinct(S)]
        derived = [[None for _ in range(7)] for _ in range(10)]
        for i in range(10):
            for j in range(7):
                x = S[j]
                derived[i][x] = signal[i][j]
#         derived = [
#             Sum([(not not ((1 << i) & n)) << S[i] for i in range(7)]) for n in signal
#         ]
#
#         B = [2, 5, 6, 0, 1, 3, 4]
#         blah = [sum((not not ((1 << i) & n)) << B[i] for i in range(7)) for n in signal]
#         print(blah)
#         print([any(g == d for g in grid) for d in blah])
#
#         match_c = [Or([(g == d) for g in grid]) for d in derived]
        s = Solver()
        s.add(range_c + unique_c + match_c)
        assert s.check() == sat
        m = s.model()
        print(m)
        mapping = {
            chr(ord("a") + i): chr(ord("a") + m.evaluate(S[i]).as_long())
            for i in range(7)
        }
        result = ["".join(sorted(s.translate(mapping))) for s in output]
        result = [digits_list.index(r) for r in result]
        print(result)

        import sys

        sys.exit()

print(total)
