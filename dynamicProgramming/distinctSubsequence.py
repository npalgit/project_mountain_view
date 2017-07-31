#!/usr/bin/python
"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
#115
REDDO: and similar ones
"""
def numDistinct(s, t):
    w = len(s)
    h = len(t)
    dp = [x[:] for x in [[0]*(w+1)]*(h+1)]
    for j in range(w+1): dp[0][j] = 1

    for i in range(1, h+1):
        for j in range(1, w+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[-1][-1]

def numDistinct_r(s, t):
    w, h = len(s), len(t)
    dp = [x[:] for x in [[0]*(w+1)]*(h+1)]

    for j in range(w+1): dp[-1][j] = 1

    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if t[i] == s[j]:
                dp[i][j] += dp[i+1][j+1]
            dp[i][j] += dp[i][j+1]

    return dp[0][0]

def numDistinct_dfs_r(s, t):
    """
    TLE 51/63
    """
    if not s and not t: return 1
    if len(s) < len(t): return 0

    return numDistinct_dfs_r(s[1:], t[1:]) + numDistinct_dfs_r(s[1:], t) \
            if t and s[0] == t[0] else numDistinct_dfs_r(s[1:], t)

def test1():
    s = 'rabbbit'
    t = 'rabbit'
    print(numDistinct(s, t))

if __name__ == '__main__':
    test1()
