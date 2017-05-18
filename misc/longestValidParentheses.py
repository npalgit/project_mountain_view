#!/usr/bin/python
"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()",
which has length = 4.

#32
REDO: everything. very tricky
"""

def lvpDp(s):
    dp = [0]*len(s)
    max_len = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                if i-dp[i-1]-2 >= 0:
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
                else:
                    dp[i] = dp[i-1]+2

            max_len = max(max_len, dp[i])

    return max_len

def lvpStack(s):
    stck = []
    stck.append(-1)
    max_len = 0

    for i, itm in enumerate(s):
        if itm == '(':
            stck.append(i)
        else:
            stck.pop()
            if not stck:
                stck.append(i)
            else:
                max_len = max(max_len, i-stck[-1])

    return max_len

def lvpTwoWay(s):
    left, right = 0, 0
    max_len = 0

    for itm in s:
        if itm == '(':
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, 2*right)
        elif right > left:
            left, right = 0, 0

    left, right = 0, 0
    for itm in s[::-1]:
        if itm == '(':
            left += 1
        else:
            right += 1

        if left == right:
            max_len = max(max_len, 2*left)
        elif left > right:
            left, right = 0, 0

    return max_len

def test1():
    s = '(((()))(())))'
    print(lvpDp(s))
    print(lvpStack(s))
    print(lvpTwoWay(s))

def test2():
    s = '(()'
    print(lvpDp(s))
    print(lvpStack(s))
    print(lvpTwoWay(s))

if __name__ == "__main__":
    test1()
    test2()
