#!/usr/bin/python
"""
Given a string S, you are allowed to convert it to a palindrome by adding characters
in front of it. Find and return the shortest palindrome you can find by performing
this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
#214
"""
def isPalin(s, b, e):
    while b < e:
        if s[b] != s[e]: return False
        b += 1
        e -= 1
    return True

def sp(s):
    """
    TLE with 119/120 passed.
    """
    if not s: return ""
    if isPalin(s, 0, len(s)-1): return s
    r = s[::-1]
    for i in range(len(r)):
        ts = r[:i+1] + s
        if isPalin(ts, i, len(ts)-i-1): return ts

def sp_lc(self, s):
    """
    lc solution. bascially same time complexity.
    """
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s
def test1():
    s = 'dedcba'
    print(sp(s))

def test2():
    s = 'aacecaabcdqa'
    print(sp(s))

if __name__ == '__main__':
    test1()
    test2()
