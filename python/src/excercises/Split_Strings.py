def split_even(s):
    for i in range(0, len(s) - 1, 2):
        yield s[i:i+2]


def solution(s):
    l = len(s)

    if l % 2 != 0:
        s += "_"

    return list(split_even(s))


print(solution("abcd"))
print(solution("abc"))