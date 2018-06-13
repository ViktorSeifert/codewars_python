def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def proper_fractions(n):
    if n == 1:
        return 0

    result = {1: True}

    for i in range(2, n):
        if i in result.keys():
            continue

        if gcd(n, i) == 1:
            result[i] = True
        else:
            result[i] = False

            for j in range(2, n // i):
                result[i * j] = False

    return len([x for x in result.items() if x[1]])


print(proper_fractions(15))
print(proper_fractions(25))
print(proper_fractions(2500000))
