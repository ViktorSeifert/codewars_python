def get_sum(a,b):
    bounds = sorted([a, b])
    result = 0
    for n in range(bounds[0], bounds[1] + 1):
        result += n
    return result

print(get_sum(1, 0) == 1) # 1 + 0 = 1
print(get_sum(1, 2) == 3) # 1 + 2 = 3
print(get_sum(0, 1) == 1) # 0 + 1 = 1
print(get_sum(1, 1) == 1) # 1
print(get_sum(-1, 0) == -1) # -1 + 0 = -1
print(get_sum(-1, 2) == 2) # -1 + 0 + 1 + 2 = 2