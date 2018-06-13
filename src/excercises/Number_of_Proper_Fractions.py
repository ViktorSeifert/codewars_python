def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def proper_fractions(n):
    if n == 1:
        return 0

    proper = set()
    proper.add(1)

    for i in range(2, n):
        if n % i == 0:
            continue

        if gcd(n, i) == 1:
            proper.add(i)

    return len(proper)


print(proper_fractions(15))
print(proper_fractions(25))
print(proper_fractions(2500000))
