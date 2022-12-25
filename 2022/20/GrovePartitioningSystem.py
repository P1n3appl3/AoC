from copy import deepcopy

nums = list(map(int, open("input").readlines()))
size = len(nums)


def flatten(state):
    start = tmp = nums.index(0)
    l = [nums[tmp]]
    while (tmp := state[tmp][1]) != start:
        l.append(nums[tmp])
    return l


def mix(state):
    for i in range(size):
        if not (cur := nums[i]):
            continue
        prev, next = state[i]
        state[prev][1] = next
        state[next][0] = prev
        tmp = prev
        for _ in range(abs(cur) % (size - 1)):
            tmp = state[tmp][1] if cur > 0 else state[tmp][0]
        state[i][0] = tmp
        next = state[i][1] = state[tmp][1]
        state[next][0] = i
        state[tmp][1] = i


initial = [[(i + size - 1) % size, (i + 1) % size] for i in range(size)]
solve = lambda l: sum(l[x % size] for x in [1000, 2000, 3000])
state = deepcopy(initial)
mix(state)
print(solve(flatten(state)))
state = deepcopy(initial)
nums = [n * 811589153 for n in nums]
for _ in range(10):
    mix(state)
print(solve(flatten(state)))
