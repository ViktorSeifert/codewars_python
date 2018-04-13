def unique_in_order(iterable):
    result = ["dummy"]
    for i in iterable:
        if i != result[-1]:
            result.append(i)

    return result[1:]

print(unique_in_order('AAAABBBCCDAABBB'))
