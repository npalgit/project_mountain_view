#!/usr/bin/python
"""
Convert a number to excel column header. Letter based. A-Z.
This essentially a converting base 10 to base 26.
#168
"""

def convert(n):
    return '' if n == 0 else convert((n-1)/26) + chr((n-1)%26+ord('A'))

def test1():
    print(convert(527))
    print(convert(837))
    print(convert(477))
    print(convert(2))

if __name__ == '__main__':
    test1()
