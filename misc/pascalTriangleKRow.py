#!/usr/bin/python
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
#119
"""

def pascalT(n):
    if n == 0: return [1]
    if n == 1: return [1,1]
    l = [1, 1]
    pt(n-1, l)

    return l

def pt(n, l):
    if n == 0: return

    for i in range(1, len(l)):
        l[i-1] = l[i-1]+l[i]
    l.insert(0, 1)
    pt(n-1, l)

def test1():
    print(pascalT(8))

def test2():
    print(pascalT(6))

if __name__ == '__main__':
    test1()
    test2()
