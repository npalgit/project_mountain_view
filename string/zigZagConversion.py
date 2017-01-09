#!/usr/bin/python
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
leetcode #6
"""

def zigZagConversion(s, l):
    lls = [x[:] for x in [[]]*l]

    li, i, sign = 0, 0, 1
    while i < len(s):
        for li in xrange(l):
            if i >= len(s):
                break

            lls[li].append(s[i])
            i += 1

        for li in xrange(l-2, 0, -1):
            if i >= len(s):
                break

            lls[li].append(s[i])
            i += 1

    # print list
    rslt = ''
    for ls in lls:
        for c in ls:
            rslt += c

    return rslt

def test1():
    s = 'PAYPALISHIRING'
    print(zigZagConversion(s, 3))

def test2():
    s = 'PAYPALISHIRINGMYGF'
    print(zigZagConversion(s, 4))

def test3():
    s = 'PAYPALISHIRING'
    print(zigZagConversion(s, 2))

def test4():
    s = 'PAYPALISHIRING'
    print(zigZagConversion(s, 1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
