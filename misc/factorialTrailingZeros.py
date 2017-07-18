#!/usr/bin/python
"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
#172
REDDO
"""
def trailingZeros(n):
    return 0 if n == 0 else n/5 + trailingZeros(n/5)

def test1():
    print(trailingZeros(27))

if __name__ == '__main__':
    test1()
