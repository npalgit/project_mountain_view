#!/usr/bin/python
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

leetcode #4
"""
def isValidP(s):
    stck = []
    for c in s:
        if c == '[' or c == '{' or c == '(':
            stck.append(c)
        elif c == ']':
            if not stck or stck.pop() != '[':
                return False
        elif c == '}':
            if not stck or stck.pop() != '{':
                return False
        elif c == ')':
            if not stck or stck.pop() != '(':
                return False
    if stck:
        return False

    return True

def test1():
    s = '[]{}[]()'
    print(isValidP(s))

def test2():
    s = '[{([])}]'
    print(isValidP(s))

def test3():
    s = '[{]}'
    print(isValidP(s))

def test4():
    s = '[]{abc}(def)'
    print(isValidP(s))

def test5():
    s = '[{('
    print(isValidP(s))

def test6():
    s = ']'
    print(isValidP(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
