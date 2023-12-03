import re
from dataclasses import dataclass
from collections import defaultdict

@dataclass(order=True, unsafe_hash=True)
class Point:
     x: int
     y: int
     def __repr__(self):
         return f"({self.x},{self.y})"

lines = []
with open("input") as f:
    for l in f:
        x1,y1,x2,y2 = map(int,re.findall(r"\d+", l))
        a,b = sorted((Point(x1, y1), Point(x2, y2)))
        lines.append((a, b))

def get_overlaps(lines):
    overlaps = defaultdict(int)
    for l in lines:
        if l[0].x == l[1].x:
            for y in range(l[0].y, l[1].y + 1):
                overlaps[Point(l[0].x, y)] += 1
        elif l[0].y == l[1].y:
            for x in range(l[0].x, l[1].x + 1):
                overlaps[Point(x, l[0].y)] += 1
        else:
            y0,y1 =  l[0].y, l[1].y
            ry = range(y0, y1 + 1)
            if y1 < y0:
                ry = range(y0, y1 - 1, -1)
            for x, y in zip(range(l[0].x, l[1].x + 1), ry):
                overlaps[Point(x, y)] += 1
    return overlaps

def diagram(lines):
    overlaps = get_overlaps(lines)
    print()
    for y in range(10):
        line = [overlaps[Point(x, y)] for x in range(10)]
        print("".join(str(n) if n > 0 else "." for n in line))
    print()


straight = list(filter(lambda l: l[0].x == l[1].x or l[0].y == l[1].y, lines))

print(len(list(filter(lambda v: v > 1, get_overlaps(straight).values()))))
# diagram(straight)

diag = list(filter(lambda l: abs(l[0].y - l[1].y) == abs(l[0].x - l[1].x), lines))

print(len(list(filter(lambda v: v > 1, get_overlaps(straight + diag).values()))))
# diagram(straight + diag)
