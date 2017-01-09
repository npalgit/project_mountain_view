#!/usr/bin/python
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
def reverseInteger(intgr):
    rslt = 0

    sign = 1
    if intgr < 0:
        sign = -1
        intgr *= -1

    while intgr > 0:
        rslt *= 10
        rslt += intgr %10
        intgr /= 10

    rslt *= sign
    intmax = 0x7fffffff
    if rslt < -intmax-1 or rslt > intmax:
        return 0
    return rslt

    return sign*rslt

def test1():
    intgr = 123
    print(reverseInteger(intgr))

def test2():
    intgr = -123
    print(reverseInteger(intgr))

def test3():
    intgr = 1200
    print(reverseInteger(intgr))

def test4():
    intgr = -1000000000
    print(reverseInteger(intgr))

def test5():
    intgr = 10003
    print(reverseInteger(intgr))

def test6():
    intgr = 1000000003
    print(reverseInteger(intgr))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
