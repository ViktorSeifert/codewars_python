class Calculator(object):
    def __init__(self):
        self.stack = []

    def add_token(self, token):
        try:
            number = float(token)
            self.stack.append(number)
        except ValueError:
            self.process_operator(token)

    def process_operator(self, operator):
        second_operand = self.stack[-1]
        first_operand = self.stack[-2]

        self.stack = self.stack[:-2]

        if operator == "+":
            op_result = first_operand + second_operand
        elif operator == "-":
            op_result = first_operand - second_operand
        elif operator == "*":
            op_result = first_operand * second_operand
        elif operator == "/":
            op_result = first_operand / second_operand

        self.stack.append(op_result)

    def value(self):
        return self.stack[-1]


def calc(expr):
    if len(expr) == 0:
        return 0

    parts = expr.split(" ")
    calc = Calculator()

    for part in parts:
        calc.add_token(part)

    return calc.value()


print(calc(""))
print(calc("1 2 3"))
print(calc("1 2 3.5"))
print(calc("1 3 -"))
print(calc("1 3 +"))
print(calc("1 3 *"))
print(calc("4 2 /"))
print(calc("1 2 3 * +"))
