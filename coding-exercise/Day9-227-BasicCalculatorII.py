"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces
The integer division should truncate toward zero.

Hitn: Uses Stack implementation
"""


def calculate(s):
    stack = []
    num = 0
    sign = "+"

    for i, c in enumerate(s):
        if c.isdigit():
            # stack.append(c)
            num = num * 10 + int(c)
        if c in ["+", "*", "/", "-"] or i + 1 == len(s):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack[-1] = stack[-1] * num
            elif sign == "/":
                stack[-1] = int(stack[-1] / float(num))
            sign = c
            num = 0
    return sum(stack)


s = " 3+5 / 2 "
print(calculate(s))
