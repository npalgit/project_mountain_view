#!/usr/bin/python
"""
Given a string s1, we may represent it as a binary tree by partitioning
it to two non-empty substrings recursively.
#87
REDDO: learn the logic, no necessarily re-write everything
"""
def scrambleString(s1, s2):
    n, m = len(s1), len(s2)
    if n != m or sorted(s1) != sorted(s2): return False
    if n < 4 or s1 == s2: return True
    f = scrambleString
    for i in range(1, n):
        if f(s1[i:], s2[i:]) and f(s1[:i], s2[:i]) or \
           f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
            return True
    return False

def test1():
    s1 = 'great'
    s2 = 'rgeta'
    print(scrambleString(s1, s2))

def test2():
    s1 = 'great'
    s2 = 'treag'
    print(scrambleString(s1, s2))

if __name__ == '__main__':
    test1()
    test2()
