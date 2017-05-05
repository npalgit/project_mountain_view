#!/usr/bin/python
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

#150
"""
def reversePN(tokens):
    """
    Got it first try with 83.82% performance
    """
    op_a, op_b = 0, 0
    stck = []

    for i in tokens:
        if i != '+' and i != '-' and i != '*' and i != '/':
            stck.append(int(i))
        else:
            op_b = stck.pop()
            op_a = stck.pop()

            if i == '+': stck.append(op_a + op_b)
            elif i == '-': stck.append(op_a - op_b)
            elif i == '*': stck.append(op_a * op_b)
            elif i == '/': stck.append(int(float(op_a) / op_b))

    return stck[0]

def test1():
    tokens = ["2", "1", "+", "3", "*"]
    print(reversePN(tokens))

def test2():
    tokens = ["4", "13", "5", "/", "+"]
    print(reversePN(tokens))

def test3():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(reversePN(tokens))

if __name__ == '__main__':
    test1()
    test2()
    test3()
