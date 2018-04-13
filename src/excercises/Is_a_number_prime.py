def is_prime(num):
    if num < 2:
        return False

    primes = [True] * (num + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, num + 1):
        if primes[i]:
            for k in range(i + i, num + 1, i):
                primes[k] = False

    return primes[num]


print(is_prime(9))
print(is_prime(7))
print(is_prime(23))
print(is_prime(21))