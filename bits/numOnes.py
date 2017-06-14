#!/usr/bin/python
"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
#191
"""
def numOnes(n):
    cnt = 0
    while n:
        if n & 1: cnt += 1
        n >>= 1
    return cnt

def test1():
    n = 0b100000001011
    print(numOnes(n))

if __name__ == '__main__':
    test1()
