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
    ["D", "E"],
]

def count_patterns_from(firstPoint, length):
    pass


print(count_patterns_from('A',10), 0)
print(count_patterns_from('A',0),  0)
print(count_patterns_from('E',14), 0)
print(count_patterns_from('B',1),  1)
print(count_patterns_from('C',2),  5)
print(count_patterns_from('E',2),  8)
print(count_patterns_from('E',4),  256)
