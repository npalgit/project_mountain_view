#!/usr/bin/python
"""
Given two integers representing the numerator and denominator of
a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in
parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

#166
REDO: very good question to redo without any help
"""

def fracToDec(top, bottom):
    res = ''
    if top/bottom < 0:
        res += '-'
    if top%bottom == 0:
        return str(top/bottom)
    top, bottom = abs(top), abs(bottom)
    res += (str(top/bottom) + '.')
    dic = {}
    i = len(res)-1
    top %= bottom

    while top != 0:
        top *= 10
        if top in dic:
            i = dic[top]
            res = res[:i] + '(' + res[i:] + ')'
            return res
        d = str(top/bottom)
        res += d
        i += 1
        dic[top] = i
        top %= bottom

    return res

def test1():
    print(fracToDec(24, 7))
    print(fracToDec(3, 7))
    print(fracToDec(38, 11))
    print(fracToDec(6, 2))
    print(fracToDec(1, 5))
    print(fracToDec(1, 333))

if __name__ == '__main__':
    test1()
