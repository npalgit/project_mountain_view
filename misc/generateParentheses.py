#!/usr/bin/python
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
leetcode #22
REDO - really good question
"""

def generateParentheses(n):
    paren = []
    generateSubP('', n, n, paren)
    return paren

def generateSubP(p, l, r, paren):
    if l:
        generateSubP(p+'(', l-1, r, paren)
    if r > l:
        generateSubP(p+')', l, r-1, paren)

    if not r:
        paren.append(p)

def test1():
    print(generateParentheses(2))

def test2():
    print(generateParentheses(3))

def test3():
    print(generateParentheses(0))

if __name__ == '__main__':
    test1()
    test2()
    test3()
