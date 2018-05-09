# this is too slow

import itertools


def decompose(n):
    target_value = n ** 2
    sub_values = list(range(1, n))
    valid_combos = []

    get_valid_combos(n, sub_values, target_value, valid_combos)

    valid_combos = sorted(valid_combos, key=lambda it: max(*it))

    if len(valid_combos) == 0:
        return None

    return list(valid_combos[-1])


def get_valid_combos(n, sub_values, target_value, valid_combos):
    for l in range(1, len(sub_values) + 1):
        combos = itertools.combinations(sub_values, l)

        for combo in combos:
            combo_sum = sum(map(lambda x: x ** 2, combo))
            if combo_sum == target_value:
                valid_combos.append(combo)
                if n - 1 in combo:
                    return


print(decompose(5))
print(decompose(11))
print(decompose(100))
