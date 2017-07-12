#!/usr/bin/python
"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

#301
REDDO: great question.
"""
from collections import deque

def removeIP(s):
    q = deque()
    visited = set()
    res = []
    if isValidP(s): return [s]
    q.append(s)
    found = False

    while q:
        s = q.popleft()
        # why continue here works? because if it is valid. There must be even number
        # of brackets. so even if the next level got added, they wouldn't qualify because
        # the next level will have odd number of brackets which won't match.
        # then you don't need to use a separate variable to denote different levels
        if isValidP(s):
            found = True
            res.append(s)

        if found: continue

        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                next_s = s[:i] + s[i+1:]
                if next_s not in visited:
                    visited.add(next_s)
                    q.append(next_s)

    return res

def isValidP(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        if count < 0: return False

    return count == 0

def test1():
    s = ')('
    print(removeIP(s))

def test2():
    s = '()())()'
    print(removeIP(s))

def test3():
    s = '(a)())()'
    print(removeIP(s))

def test4():
    s = '(((k()(('
    print(removeIP(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
