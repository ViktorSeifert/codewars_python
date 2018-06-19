import math


def race(v1, v2, g):
    if v1 >= v2:
        return None

    t = g / (v2-v1)

    h = math.floor(t)
    m = math.floor((t * 60.0) - (h * 60.0))
    s = math.floor((t * 3600.0) - (h * 3600.0) - (m * 60.0))

    return [h, m, s]


print(race(720, 850, 70))
print(race(80, 91, 37))
print(race(80, 100, 40))
print(race(-1, 15, 20))
