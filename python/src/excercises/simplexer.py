import re

OPERATORS = ["+", "-", "*", "/", "%", "(", ")", "="]

KEYWORDS = ["if", "else", "for", "while", "return", "func", "break"]

BOOLEANS = ["true", "false"]


class Token(object):
    def __init__(self, text, type=None):
        if text is None:
            text = ""

        self.text = text

        if type is None:
            self.type = self.determine_type()
        else:
            self.type = type

    def __repr__(self):
        return "T(" + self.text + "|" + self.type + ")"

    def __eq__(self, other):
        if other is Token:
            return False

        return self.text == other.text and self.type == other.type

    def determine_type(self):
        if self.text.isdigit():
            return "integer"

        if self.text in BOOLEANS:
            return "boolean"

        if self.text in KEYWORDS:
            return "keyword"

        if self.text in OPERATORS:
            return "operator"

        if self.text.isspace():
            return "whitespace"

        if re.fullmatch("[a-zA-Z$_][a-zA-Z$_0-9]*", self.text) is not None:
            return "identifier"

        if self.text[0] == '"' and self.text[len(self.text) - 1]:
            return "string"

        return "unknown"


class Simplexer(object):
    def __init__(self, expression):
        self.__expression = expression
        self.__it = self.__iter__()

    def __iter__(self):
        index = 0

        while index < len(self.__expression):
            token_text, index = self.token_text_at(index)
            yield Token(token_text)

    def __next__(self):
        next(self.__it)

    def token_text_at(self, index):
        result = ""
        initial_letter_category = self.letter_category(self.__expression[index])

        while index < len(self.__expression) \
                and self.letter_category(self.__expression[index]) == initial_letter_category:
            result += self.__expression[index]
            index += 1

        return result, index

    @staticmethod
    def letter_category(letter):
        if letter.isspace():
            return 0

        if letter in OPERATORS:
            return OPERATORS.index(letter) + 1

        return -1


def tester(strng, tokenLst):
    print("Testing " + str(strng))
    simplex = Simplexer(strng)
    result = [t for t in simplex]
    print("Expected: " + str(tokenLst) + "\nReceived: " + str(result))
    assert result == tokenLst


tester("x", [Token("x", "identifier")])
tester("true", [Token("true", "boolean")])
tester("12345", [Token("12345", "integer")])
tester('"String"', [Token('"String"', "string")])
tester("break", [Token("break", "keyword")])

test_string = "(1 + 2) - 5"
tokens = ["(", "1", " ", "+", " ", "2", ")", " ", "-", " ", "5"]
token_types = ["operator", "integer", "whitespace", "operator",
               "whitespace", "integer", "operator", "whitespace",
               "operator", "whitespace", "integer"]
tester(test_string, [Token(a, b) for a, b in zip(tokens, token_types)])

test_string = "return x + 1"
tokens = ["return", " ", "x", " ", "+", " ", "1"]
token_types = ["keyword", "whitespace", "identifier", "whitespace", "operator", "whitespace", "integer"]
tester(test_string, [Token(a, b) for a, b in zip(tokens, token_types)])
