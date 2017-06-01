#!/usr/bin/python
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
#139
"""
from collections import deque
def wBreakDp(s, wList):
    wSet = set(wList)
    dp = [False]*(len(s)+1)
    dp[0] = True

    for j in range(1, len(s)+1):
        for i in range(1, j+1):
            dp[j] = dp[i-1] and (s[i-1:j] in wSet)
            if dp[j]: break
    return dp[-1]

def wBreakBFS(s, wList):
    if not s: return False
    wSet = set(wList)
    visited = [False]*len(s)
    q = deque()
    q.append(0)
    while q:
        start = q.popleft()
        for end in range(start, len(s)):
            if not visited[end] and s[start:end+1] in wSet:
                if end == len(s)-1: return True
                visited[end] = True
                q.append(end+1)
    return False

def wBreak(s, wList):
    """
    Brute force, dfs, TLE
    """
    wSet = set(wList)
    return dfs(s, wSet)

def dfs(s, wSet):
    if not s: return True
    for i in range(len(s)):
        if s[:i+1] in wSet and dfs(s[i+1:], wSet):
            return True

    return False

def test1():
    s = 'abcdefghi'
    wList = ['abc', 'def', 'ghi']
    print(wBreak(s, wList))
    print(wBreakDp(s, wList))
    print(wBreakBFS(s, wList))
    print('------------------')

def test2():
    s = 'leetcode'
    wList = ['le', 'et', 'co', 'code']
    print(wBreak(s, wList))
    print(wBreakDp(s, wList))
    print(wBreakBFS(s, wList))
    print('------------------')

def test3():
    s = 'leetcode'
    wList = ['leet', 'cod']
    print(wBreak(s, wList))
    print(wBreakDp(s, wList))
    print(wBreakBFS(s, wList))
    print('------------------')

def test4():
    s = 'abcdef'
    wList = ['a', 'b', 'c', 'd', 'e', 'f']
    print(wBreak(s, wList))
    print(wBreakDp(s, wList))
    print(wBreakBFS(s, wList))
    print('------------------')

def test5():
    s = 'a'
    wList = ['a']
    print(wBreak(s, wList))
    print(wBreakDp(s, wList))
    print(wBreakBFS(s, wList))
    print('------------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
