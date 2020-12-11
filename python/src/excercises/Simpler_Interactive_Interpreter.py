# https://www.codewars.com/kata/53005a7b26d12be55c000243/train/python

import re
from enum import Enum, auto


OPERATOR_PATTERN = "[-+*\/\%=\(\)]"
IDENTIFIER_PATTERN = "[A-Za-z_][A-Za-z0-9_]*"
NUMBER_PATTERN = "[0-9]*\.?[0-9]+"
VALID_TOKENS_PATTERN = "\s*(=>|" + OPERATOR_PATTERN + "|" + IDENTIFIER_PATTERN + "|" + NUMBER_PATTERN + ")\s*"
# the following regex should capture all invalid tokens but it does not as it is
INVALID_TOKENS_PATTERN = "(?!" + OPERATOR_PATTERN + "|" + IDENTIFIER_PATTERN + "|" + NUMBER_PATTERN + ")"


def tokenize(expression):
    invalid_tokens = [s for s in re.compile(INVALID_TOKENS_PATTERN).findall(expression) if not (s.isspace or s == "")]
    if len(invalid_tokens) > 0:
        raise ValueError

    valid_tokens_regex = re.compile(VALID_TOKENS_PATTERN)
    tokens = valid_tokens_regex.findall(expression)
    return [Token(s) for s in tokens if not s.isspace()]


class TokenType(Enum):
    UNKNOWN = auto()
    NUMBER = auto()
    OPERATOR = auto()
    IDENTIFIER = auto()
    OPEN_BRACE = auto()
    CLOSE_BRACE = auto()


class Token:
    IDENTIFIER_PATTERN = re.compile(IDENTIFIER_PATTERN)

    def __init__(self, input):
        self.content = input
        self.type = TokenType.UNKNOWN

        if self._is_number(self.content):
            self.type = TokenType.NUMBER
        elif self._is_operator(self.content):
            self.type = TokenType.OPERATOR
        elif self._is_identifier(self.content):
            self.type = TokenType.IDENTIFIER
        elif self.content == "(":
            self.type = TokenType.OPEN_BRACE
        elif self.content == ")":
            self.type = TokenType.CLOSE_BRACE

    @staticmethod
    def _is_number(a_string):
        try:
            float(a_string)
            return True
        except ValueError:
            return False

    @staticmethod
    def _is_operator(content):
        return content in {"+", "-", "*", "/", "%"}

    def __repr__(self):
        return '<' + str(self.type) + ' ' + self.content + '>'

    def value(self):
        if self.type == TokenType.NUMBER:
            return float(self.content)
        else:
            return self.content

    @staticmethod
    def _is_identifier(content):
        return bool(Token.IDENTIFIER_PATTERN.fullmatch(content))


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        if expression.isspace():
            return ""
        else:
            tokens = tokenize(expression)
            print("tokens: " + str(tokens))


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
        print("!!! no exception !!!")
    except Exception as ex:
        print("caught exception: " + str(ex))

    print("------------------------------")


def run_tests():
    assert_equals("1 + 1", 2)
    assert_equals("(1 + 1)", 2)
    assert_equals("2 - 1", 1)
    assert_equals("2 * 3", 6)
    assert_equals("8 / 4", 2)
    assert_equals("7 % 4", 3)

    assert_equals("x = 1", 1)
    assert_equals("x", 1)
    assert_equals("x + 3", 4)
    assert_equals(" ", "")
    expect_error("y")
    expect_error("4 # 2")


run_tests()
