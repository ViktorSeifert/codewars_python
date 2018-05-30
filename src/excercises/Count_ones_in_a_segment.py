def increment(bin_str):
    ones = 0

    bin_str = list(bin_str)

    carry = 1
    for i in range(len(bin_str) - 1, 0, -1):
        value = bin_str[i]

        if value == "1":
            ones += 1

        if carry == 1:
            if value == "1":
                carry = 1
                value = "0"
            else:
                carry = 0
                value = "1"

        bin_str[i] = value

    return "".join(bin_str), ones


def countOnes(left, right):
    sum = 0

    bin_str = "{0:048b}".format(left)
    bin_stop = "{0:048b}".format(right + 1)

    while bin_str != bin_stop:
        bin_str, ones = increment(bin_str)
        sum += ones

    return sum


print(countOnes(5, 7))
print(countOnes(12, 29))