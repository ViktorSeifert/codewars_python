def valid_parentheses(string):
    count = 0
    for c in string:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses("hi(hi)()"))