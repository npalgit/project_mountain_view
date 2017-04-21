#!/usr/bin/python
"""
Given a roman numeral convert to integer.
#13
"""
def roman2Int(r):
    dic = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0

    i = 0
    while i < len(r):
        if i+1 < len(r) and dic[r[i]] < dic[r[i+1]]:
            v = dic[r[i+1]] - dic[r[i]]
            i += 2
        else:
            v = dic[r[i]]
            i += 1
        num += v

    return num

def test1():
    print(roman2Int('XLI'))
    print('------------')

def test2():
    print(roman2Int('LXXV'))
    print('------------')

def test3():
    print(roman2Int('MCMLIV'))
    print('------------')

def test4():
    print(roman2Int('MMXIV'))
    print('------------')

def test5():
    print(roman2Int('M'))
    print('------------')

def test6():
    print(roman2Int(''))
    print('------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
