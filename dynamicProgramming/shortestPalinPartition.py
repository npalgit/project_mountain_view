#!/usr/bin/python
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#132
REDDO: review both solutions, optionally coding them.
"""
def shortestPalinPart(s):
    """
    first solution TLE at 26/29 test cases
    """
    if not s: return 0
    dp = [x[:] for x in [[0]*len(s)]*len(s)]

    for beg in reversed(range(len(s))):
        for end in range(beg, len(s)):
            if isPalin(s[beg:end+1]):
                dp[beg][end] = 0
            else:
                dp[beg][end] = min([dp[beg][m]+dp[m+1][end] for m in range(beg, end)])+1
    return dp[0][-1]

def minCut_r(s):
    n = len(s)
    dp = [x[:] for x in [[False]*n]*n]
    cut = [0]*n

    for j in range(n):
        cut[j] = j
        for i in reversed(range(j+1)):
            if s[i] == s[j] and (i+1 >= j-1 or dp[i+1][j-1]):
                dp[i][j] = True
                if i == 0:
                    cut[j] = 0
                    # break, optional
                else:
                    cut[j] = min(cut[j], cut[i-1]+1)
    return cut[-1]

def isPalin(s):
    return s == s[::-1]

def shortestPalinPartFaster(s):
    if not s: return 0
    n = len(s)
    cut = [0]*n
    isPali = [x[:] for x in [[False]*n]*n]

    for j in range(n):
        min_v = j
        for i in range(j+1):
            if s[i] == s[j] and (i+1 >= j-1 or isPali[i+1][j-1]):
                isPali[i][j] = True
                if i == 0:
                    min_v = 0
                    break
                min_v = min(min_v, cut[i-1]+1)
        cut[j] = min_v

    return cut[-1]

def minCut_dfs_r(s):
    """
    21/29 TLE
    """
    if isPalin(s): return 0
    min_cut = len(s)
    for i in range(1, len(s)):
        min_cut = min(min_cut, (minCut_dfs_r(s[:i]) + minCut_dfs_r(s[i:])))
    return min_cut+1

def test1():
    s = 'cabaca'
    print(shortestPalinPart(s))
    print(shortestPalinPartFaster(s))

def test2():
    s = 'cabacaxyz'
    print(shortestPalinPart(s))
    print(shortestPalinPartFaster(s))

def test3():
    s = ''
    print(shortestPalinPart(s))
    print(shortestPalinPartFaster(s))

def test4():
    s = 'leet'
    print(shortestPalinPart(s))
    print(shortestPalinPartFaster(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
