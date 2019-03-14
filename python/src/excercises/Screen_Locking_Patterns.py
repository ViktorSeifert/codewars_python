# https://www.codewars.com/kata/585894545a8a07255e0002f1/train/python

point_map = [
    ["A", "B"],
    ["A", "B", "C"],
    ["A", "D"],
    ["A", "D", "G"],
    ["A", "E"],
    ["A", "E", "I"],
    ["A", "F"],
    ["A", "H"],
    ["B", "C"],
    ["B", "D"],
    ["B", "E"],
    ["B", "E", "H"],
    ["B", "F"],
    ["B", "G"],
    ["B", "I"],
    ["C", "D"],
    ["C", "E"],
    ["C", "E", "G"],
    ["C", "F"],
    ["C", "F", "I"],
    ["C", "H"],
    ["D", "E"],
    ["D", "E", "F"],
    ["D", "G"],
    ["D", "H"],
    ["D", "I"],
    ["E", "F"],
    ["E", "G"],
    ["E", "H"],
    ["E", "I"],
    ["F", "G"],
    ["F", "H"],
    ["F", "I"],
    ["G", "H"],
    ["G", "H", "I"],
    ["H", "I"],
]


def all_direct_paths_from(point):
    for p in point_map:
        if p[0] == point:
            yield p
        elif p[-1] == point:
            p = p[:]
            p.reverse()
            yield p


def count_patterns_from(firstPoint, length):
    if length <= 0:
        return 0
    patterns = []
    patterns_recur([firstPoint], length - 1, patterns)
    return len(patterns)


def concat(pattern, path):
    new_pattern = pattern[:]
    for p in path:
        if p not in new_pattern:
            new_pattern.append(p)
    return new_pattern


def patterns_recur(pattern, length, patterns):
    if length < 0:
        return

    if length == 0 and pattern not in patterns:
        patterns.append(pattern)
        return

    for path in all_direct_paths_from(pattern[-1]):
        new_pattern = concat(pattern, path)
        if new_pattern != pattern:
            patterns_recur(new_pattern, length - (len(new_pattern) - len(pattern)), patterns)


print(count_patterns_from('A', 10), 0)
print(count_patterns_from('A', 0), 0)
print(count_patterns_from('E', 14), 0)
print(count_patterns_from('B', 1), 1)
print(count_patterns_from('C', 2), 5)
print(count_patterns_from('E', 2), 8)
print(count_patterns_from('E', 4), 256)
