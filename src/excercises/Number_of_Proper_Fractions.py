from __future__ import print_function, division


def prime_numbers(num):
    primes = [True] * (num + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, num + 1):
        if primes[i]:
            for k in range(i + i, num + 1, i):
                primes[k] = False

    result = []

    for i, prime in enumerate(primes):
        if prime and i > 0:
            result.append(i)

    return result


def prime_factors(n):
    primes = prime_numbers(n)

    factors = []

    for i in primes:
        if gcd(n, i) > 1:
            factors.append(i)

    return factors


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def proper_fractions(n):
    if n == 1:
        return 0

    result = 1.

    for factor in prime_factors(n):
        part = (1 - (1 / factor))
        result *= part

    return int(result * n)


print(proper_fractions(1))
print(proper_fractions(2))
print(proper_fractions(5))
print(proper_fractions(15))
print(proper_fractions(25))
print(proper_fractions(2500000))
