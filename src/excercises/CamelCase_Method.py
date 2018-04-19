def camel_case(string):
    parts = string.split(" ")

    result = ""

    for part in (p for p in parts if p != ""):
        result += part[:1].upper() + part[1:]

    return result


print(camel_case("test case"))
print(camel_case("camel case method"))
print(camel_case(" camel case word"))
