#!/usr/bin/python
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
#201
REDO: smart algorithm
"""
def bitAndRange(m, n):
    if m == 0: return 0
    moveFac = 0
    while m != n:
        moveFac += 1
        m >>= 1
        n >>= 1

    return m<<moveFac

def bitAndRange2(m, n):
    if m == 0: return 0
    moveFac = 1
    while m != n:
        moveFac << 1
        m >>= 1
        n >>= 1

    return m*moveFac

def test1():
    print(bitAndRange(4, 7))

if __name__ == '__main__':
    test1()
