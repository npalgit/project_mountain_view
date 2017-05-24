#!/usr/bin/python
"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

#97
"""
def interleaveString(s1, s2, s3):
    w = len(s1)
    h = len(s2)
    if len(s3) != (w+h): return False
    dp = [x[:] for x in [[False]*(w+1)]*(h+1)]
    dp[0][0] = True
    for j in range(1, w+1):
        if s1[j-1] == s3[j-1] and dp[0][j-1] == True: dp[0][j] = True

    for i in range(1, h+1):
        if s2[i-1] == s3[i-1] and dp[i-1][0] == True: dp[i][0] = True

    for j in range(1, w+1):
        for i in range(1, h+1):
            if (dp[i-1][j] == True and s2[i-1] == s3[i+j-1]) or \
                (dp[i][j-1] == True and s1[j-1] == s3[i+j-1]):
                dp[i][j] = True

    return dp[-1][-1]

def interleaveStringLessSpace(s1, s2, s3):
    w = len(s1)
    h = len(s2)

    if len(s3) != (w+h): return False
    dp = [False]*(w+1)
    for i in range(h+1):
        for j in range(w+1):
            if j == 0 and i == 0: dp[j] = True
            elif i == 0:
                dp[j] = s1[j-1] == s3[j-1] and dp[j-1]
            elif j == 0:
                dp[j] = s2[i-1] == s3[i-1] and dp[j]
            else:
                dp[j] = (dp[j] and s2[i-1] == s3[i+j-1]) or \
                (dp[j-1] and s1[j-1] == s3[i+j-1])

    return dp[-1]

def test1():
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print(interleaveString(s1, s2, s3))
    print(interleaveStringLessSpace(s1, s2, s3))
    print('----------------')

def test2():
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbbaccc'
    print(interleaveString(s1, s2, s3))
    print(interleaveStringLessSpace(s1, s2, s3))
    print('----------------')

def test3():
    s1 = ''
    s2 = ''
    s3 = ''
    print(interleaveString(s1, s2, s3))
    print(interleaveStringLessSpace(s1, s2, s3))
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
