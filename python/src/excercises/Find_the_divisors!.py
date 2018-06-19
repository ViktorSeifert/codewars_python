def divisors(integer):
    divs = [n for n in range(2, integer) if integer % n == 0]

    if len(divs) == 0:
        return "{} is prime".format(integer)

    return divs


print(divisors(15))
print(divisors(12))
print(divisors(13))
