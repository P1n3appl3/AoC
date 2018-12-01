with open("input.txt") as f:
    level = 0
    score = 0
    garbageCount = 0
    while True:
        current = f.read(1)
        if not current:
            break
        if current == '{':
            level += 1
            score += level
        elif current == '}':
            level -= 1
        elif current == '!':
            f.read(1)
        elif current == '<':
            while current != '>':
                current = f.read(1)
                if current == '!':
                    f.read(1)
                else:
                    garbageCount += 1
            garbageCount -= 1

print "Part 1:", score
print "Part 2:", garbageCount
