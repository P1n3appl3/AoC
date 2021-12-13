points = []
folds = []
with open("input") as f:
    done = False
    for line in f:
        temp = line.strip()
        if not done and temp:
            a, b = temp.split(",")
            points.append((int(a), int(b)))
        else:
            if not done:
                done = True
                continue
            axis, num = line.split("=")
            folds.append((axis[-1], int(num)))


def fold(pts, fold):
    axis, pos = fold
    new = []
    for p in pts:
        x, y = p
        if axis == "y" and y > pos:
            y = pos - (y - pos)
        elif axis == "x" and x > pos:
            x = pos - (x - pos)
        new.append((x, y))
    return new


print(len(set(fold(points, folds[0]))))

for f in folds:
    points = fold(points, f)

for y in range(10):
    print("".join("X" if (x, y) in points else " " for x in range(50)))
