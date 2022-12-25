from operator import ge, sub

ORE, CLAY, OBS, GEO = range(4)
build = lambda t, r: t[:r] + (t[r] + 1,) + t[r + 1 :]
take = lambda a, b: tuple(map(sub, a, b))
better = enough = lambda a, b: all(map(ge, a, b))
worse = lambda a, b: all(map(lt, a, b))


# naive tree search is too slow, have to memoize or eary cutoff somehow
# is it ever suboptimal to build a geo bot when you can?
def rec(prices, bots, mats, score, t):
    # print(t, bots, mats)
    new_mats = tuple(a + b for a, b in zip(bots, mats))
    if not t:
        return score
    best = score
    if enough(mats, prices[GEO]):
        return rec(prices, bots, take(new_mats, prices[GEO]), score + t - 1, t - 1)
    for i in range(3):
        if enough(mats, prices[i]):
            tmp = rec(prices, build(bots, i), take(new_mats, prices[i]), score, t - 1)
            best = max(best, tmp)
    best = max(best, rec(prices, bots, new_mats, score, t - 1))
    return best


def best(blueprint):
    ore, clay, obs_ore, obs_clay, geo_ore, geo_obs = blueprint
    prices = (
        (ore, 0, 0),
        (clay, 0, 0),
        (obs_ore, obs_clay, 0),
        (geo_ore, 0, geo_obs),
    )
    bots = (1, 0, 0)
    mats = (0, 0, 0)
    return rec(prices, bots, mats, 0, 24)


blueprints = [tuple(int(x) for x in s.split() if x.isnumeric()) for s in open("small")]
print(best(blueprints[0]))
# print(sum(map(best, blueprints)))
