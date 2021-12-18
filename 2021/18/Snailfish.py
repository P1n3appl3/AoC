import math
import copy
from functools import reduce as fold


def add_first(l, dir, n):
    if type(l[dir]) is list:
        add_first(l[dir], dir, n)
    else:
        l[dir] += n


def try_explode(l, d=0):
    # print("exploding:", l, d)
    a, b = l
    if d == 3:
        if type(a) is list:
            temp = tuple(a)
            l[0] = 0
            if type(b) is int:
                l[1] += temp[1]
            else:
                add_first(b, 0, temp[1])
            return ("l", temp[0])
        elif type(b) is list:
            temp = tuple(b)
            l[1] = 0
            if type(a) is int:
                l[0] += temp[0]
            else:
                add_first(a, 1, temp[0])
            return ("r", temp[1])
        return False
    if type(a) is list:
        result = try_explode(a, d + 1)
        if result:
            if type(result) is tuple:
                # print("result", result, l)
                dir, n = result
                if dir == "l":
                    return result
                if type(b) is int:
                    l[1] += n
                else:
                    add_first(b, 0, n)
            return True
    if type(b) is list:
        result = try_explode(b, d + 1)
        if result:
            if type(result) is tuple:
                dir, n = result
                if dir == "r":
                    return result
                if type(a) is int:
                    l[0] += n
                else:
                    add_first(a, 1, n)
            return True
    return False


split = lambda n: [n // 2, math.ceil(n / 2)]


def try_split(l):
    a, b = l
    if type(a) is list:
        if try_split(a):
            return True
    elif a > 9:
        l[0] = split(a)
        return True
    if type(b) is list:
        if try_split(b):
            return True
    elif b > 9:
        l[1] = split(b)
        return True
    return False


def reduce(l):
    while True:
        if try_explode(l):
            # print(l, "explode")
            continue
        if try_split(l):
            # print(l, "split")
            continue
        # print("done reducing")
        break


def add(l, r):
    temp = [copy.deepcopy(l), copy.deepcopy(r)]
    # print(temp, "after add")
    reduce(temp)
    return temp


# explode_tests = [
#     ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
#     ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
#     ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
#     (
#         [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
#         [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
#     ),
#     ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]),
# ]
# for a, b in explode_tests:
#     try_explode(a)
#     if str(a) != str(b):
#         print(a, "should be", b)


# print(add([[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]))


def magnitude(l):
    a, b = l
    return 3 * (a if type(a) is int else magnitude(a)) + 2 * (
        b if type(b) is int else magnitude(b)
    )


# test_magnitude = [
#     ([[1, 2], [[3, 4], 5]], 143),
#     ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
#     ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
#     ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
#     ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
#     ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
# ]
#
# for l, n in test_magnitude:
#     if magnitude(l) != n:
#         print(l, "should be", n, f"(was {magnitude(l)})")

nums = list(map(eval, open("input").readlines()))
print(magnitude(fold(add, nums)))

most = 0
for a in range(len(nums)):
    for b in range(len(nums)):
        if a == b:
            continue
        most = max(magnitude(add(nums[a], nums[b])), most)
print(most)
