#!/usr/bin/python
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

leetcode #29
REDO: sol very efficient way of dividing.
"""
def d2Int(t, b):
    # when xor, sgn = 1, if neg
    #           sgn = 0, if pos
    sgn = (t < 0) ^ (b < 0)
    t = abs(t)
    b = abs(b)
    rslt = 0

    while t >= b:
        temp_b = b
        i = 1

        # exponential growth
        while t >= temp_b:
            t -= temp_b
            rslt += i
            i <<= 1
            temp_b <<= 1
    if sgn:
        rslt = -rslt

    int_max = 0x7fffffff
    int_min = -int_max-1
    return min(max(int_min, rslt), int_max)

def test1():
    print(d2Int(100, 2))

def test2():
    print(d2Int(7, 2))


def test3():
    print(d2Int(-100, 2))

def test4():
    print(d2Int(-100, -3))

def test5():
    print(d2Int(-5, 100))

def test6():
    print(d2Int(-2147483648, -1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
