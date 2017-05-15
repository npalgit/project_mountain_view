#!/usr/bin/python
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

#91
"""
def decodeWays(s):
    if not s or s[0] == '0': return 0
    rslt = [0]*(len(s)+1)
    rslt[0], rslt[1] = 1, 1

    for i in range(2, len(rslt)):
        vm1 = int(rslt[i-1]) if s[i-1] != '0' else 0
        twoV = int(s[i-2:i])
        vm2 = int(rslt[i-2]) if twoV >= 10 and twoV <= 26 else 0
        if vm1+vm2 == 0: return 0
        rslt[i] = vm1+vm2

    return rslt[-1]

def test1():
    print(decodeWays('2134718'))
    print(decodeWays('21003'))
    print(decodeWays('2134208'))
    print(decodeWays('1000001'))
    print(decodeWays('0'))
    print(decodeWays(''))
    print(decodeWays('10'))

if __name__ == '__main__':
    test1()
