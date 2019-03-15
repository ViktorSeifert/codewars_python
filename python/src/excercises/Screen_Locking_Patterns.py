# https://www.codewars.com/kata/585894545a8a07255e0002f1/train/python

points = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

pass_through_point_map = [
    ["A", "B", "C"],
    ["A", "D", "G"],
    ["A", "E", "I"],
    ["B", "E", "H"],
    ["C", "E", "G"],
    ["C", "F", "I"],
    ["D", "E", "F"],
    ["G", "H", "I"],
]


def get_path_extension_cost(pattern, point):
    a = pattern[-1]

    for p in pass_through_point_map:
        if (a == p[0] and point == p[2] and p[1] not in pattern)\
                or (a == p[-1] and point == p[0] and p[1] not in pattern):
            return 2

    return 1


def extend_patterns(patterns):
    result = []
    for pattern in patterns:
        remaining_points = set(points[:]) - set(pattern)
        for point in remaining_points:
            cost = get_path_extension_cost(pattern, point)
            if cost == 1:
                result.append(pattern + [point])

    return result


def count_patterns_from(first_point, length):
    if length <= 0:
        return 0

    remaining_length = length - 1
    patterns = [[first_point]]

    while remaining_length > 0:
        patterns = extend_patterns(patterns)
        remaining_length -= 1

    return len([i for i in patterns if len(i) == length])


print(count_patterns_from('A', 10), 0)
print(count_patterns_from('A', 0), 0)
print(count_patterns_from('E', 14), 0)
print(count_patterns_from('B', 1), 1)
print(count_patterns_from('C', 2), 5)
print(count_patterns_from('E', 2), 8)
print(count_patterns_from('E', 4), 256)
