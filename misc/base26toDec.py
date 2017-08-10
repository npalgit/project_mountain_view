#!/usr/bin/python
"""
this problem is basicaly base 26 to base 10.
#171
"""

def base26toDec(s):
    rslt = 0
    for idx, c in enumerate(reversed(s)):
        rslt += (ord(c)-ord('A')+1)*pow(26, idx)
    return rslt

def test1():
    print(base26toDec('TG'))
    print(base26toDec('AFE'))
    print(base26toDec('RI'))
    print(base26toDec('B'))
    print(base26toDec('Z'))

if __name__ == '__main__':
    test1()
