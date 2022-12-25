trans = "=-012"


def to_dec(snafu):
    places = tuple(trans.index(c) - 2 for c in snafu)
    place = 1
    total = 0
    for n in places[::-1]:
        total += place * n
        place *= 5
    return total


def to_snafu(dec):
    places = []
    while dec > 0:
        tmp = dec % 5
        places.append((tmp + 2) % 5)
        if tmp > 2:
            dec += 5
        dec //= 5
    return "".join(trans[i] for i in places[::-1])


total = 0
for line in open("input"):
    total += to_dec(line.strip())

print(total, to_snafu(total))
