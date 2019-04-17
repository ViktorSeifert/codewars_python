# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/train/python
# this is unsolved


def height(n, m):
    if n == 0 or m == 0:
        return 0

    if m == 1:
        return 1

    if n == 1:
        return 1

    return (n + 1) * m


print(height(2, 14))
print(height(7, 20))
