def xo(s):
    exes = 0
    ohs = 0

    for char in s.lower():
        if char == "x":
            exes += 1
        elif char == "o":
            ohs += 1

    return exes == ohs

print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))