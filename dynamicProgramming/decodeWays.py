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

def decodeWays_r(s):
    if not s: return 0
    dp = [0]*(len(s)+1)
    dp[-1] = 1
    dp[-2] = 1 if s[-1] != '0' else 0
    for i in reversed(range(len(s)-1)):
        if s[i] == '0':
            continue

        dp[i] = dp[i+1]
        if int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
            dp[i] += dp[i+2]

    return dp[0]

def test1():
    print(decodeWays('2134718'))
    print(decodeWays_r('2134718'))
    print('--------------')
    print(decodeWays('21003'))
    print(decodeWays_r('21003'))
    print('--------------')
    print(decodeWays('2134208'))
    print(decodeWays_r('2134208'))
    print('--------------')
    print(decodeWays('1000001'))
    print(decodeWays_r('1000001'))
    print('--------------')
    print(decodeWays('0'))
    print(decodeWays_r('0'))
    print('--------------')
    print(decodeWays(''))
    print(decodeWays_r(''))
    print('--------------')
    print(decodeWays('10'))
    print(decodeWays_r('10'))
    print('--------------')
    print(decodeWays('10241201'))
    print(decodeWays_r('10241201'))

if __name__ == '__main__':
    test1()
