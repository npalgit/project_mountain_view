#!/usr/bin/python
"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
leetcode #9
"""
def int2Roman(n):
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    M = ['', 'M', 'MM', 'MMM']

    s =  M[n/1000] + C[(n/100)%10] + X[(n/10)%10] + I[n%10]
    return s

def test1():
    print(int2Roman(41))
    print('------------')

def test2():
    print(int2Roman(75))
    print('------------')

if __name__ == '__main__':
    test1()
    test2()
