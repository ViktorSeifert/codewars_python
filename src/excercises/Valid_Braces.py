openers = ["(", "[", "{"]
closers = [")", "]", "}"]


def closes(opener, closer):
    round = opener == "(" and closer == ")"
    curly = opener == "{" and closer == "}"
    square = opener == "[" and closer == "]"

    return round or curly or square


def validBraces(string):
    stack = []

    for current in string:
        if current in openers:
            stack.append(current)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if not closes(opener=top, closer=current):
                return False

    return len(stack) == 0


print(validBraces("()"))
print(validBraces("({})"))
print(validBraces("({}])"))
print(validBraces("(((({{"))
print(validBraces("[]"))
