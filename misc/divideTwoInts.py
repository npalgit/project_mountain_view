#!/usr/bin/python
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

leetcode #29
REDDO: sol very efficient way of dividing.
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

def divide_r(self, top, bottom):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        int_max = 0x7fffffff
        int_min = -int_max-1
        if top == int_min and bottom == -1:
            return int_max
        sgn = (top < 0) ^ (bottom < 0)
        top = abs(top)
        bottom = abs(bottom)
        res = 0
        while bottom <= top:
            temp_b = bottom

            i = 1
            while temp_b <= top:
                top -= temp_b
                res += i
                i <<= 1
                temp_b <<= 1

        return -res if sgn else res
 # ------------- redo- not expoential inrease, gives TLE --------
def divide_not_exp_r(top, bottom):
    int_max = 0x7fffffff
    int_min = -int_max-1
    if top == int_min and bottom == -1:
        return int_max
    sign = 1
    if top < 0 and bottom < 0:
        top = ~top+1
        bottom = ~bottom+1
    elif top < 0 and bottom > 0:
        sign = -1
        top = ~top+1
    elif top > 0 and bottom < 0:
        sign = -1
        bottom = ~bottom+1

    if top < bottom or bottom == 0:
        return 0

    half = bottom
    count = 2
    even_odd = 0
    while True:
        s_mul = half+half if even_odd == 0 else half+half+bottom
        if s_mul > top:
            return count-1 if sign == 1 else ~(count-1)+1
        count += 1
        even_odd += 1

        if even_odd == 2:
            even_odd = 0
            half += bottom

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
