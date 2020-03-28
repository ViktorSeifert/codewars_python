# https://www.codewars.com/kata/53005a7b26d12be55c000243/train/python

import re


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        tokens = tokenize(expression)


def assert_equals(input, expected):
    print("input: " + str(input))

    print("expected: " + str(expected))

    interpreter = Interpreter()
    try:
        result = interpreter.input(input)
    except Exception as exception:
        result = exception
    print("result: " + str(result))

    if result == expected:
        print("Correct")
    else:
        print("!!! Failed !!!")

    print("------------------------------")


def expect_error(inpput):
    print("input: " + str(input))

    print("expected Exception")

    interpreter = Interpreter()
    try:
        interpreter.input(inpput)
    except:
        print("caught exception")
        return

    print("!!! no exception !!!")


def run_tests():
    assert_equals("1 + 1", 2)
    assert_equals("2 - 1", 1)
    assert_equals("2 * 3", 6)
    assert_equals("8 / 4", 2)
    assert_equals("7 % 4", 3)

    assert_equals("x = 1", 1)
    assert_equals("x", 1)
    assert_equals("x + 3", 4)
    expect_error("y")

run_tests()
