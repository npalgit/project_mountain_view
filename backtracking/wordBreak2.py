#!/usr/bin/python
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
#140
REDDO: dfs_mem, dp_mem, time complexity
"""

from collections import deque
import copy

def containsSuffix(s, wSet):
    for i in range(len(s)):
        if s[i:] in wSet:
            return True
    return False

def wordBreakSS(s, wList):
    """
    Accepted solution.
    """
    mem = {}
    wSet = list(wList)
    return wordBreakSSHelper(s, wSet, mem)

def wordBreakSSHelper(s, wSet, mem):
    if s in mem: return mem[s]

    rslt = []
    if s in wSet: rslt.append(s)
    for i in range(len(s)):
        left, right = s[:i+1], s[i+1:]
        # contiansSuffix speeds things up a little
        if left in wSet and containsSuffix(right, wSet):
            for ws_r in wordBreakSSHelper(right, wSet, mem):
                rslt.append(left + ' ' + ws_r)

    mem[s] = rslt
    return rslt

def wordBreakDFS(s, wList):
    """
    29/37 passed. TLE
    """
    wSet = set(wList)
    rslt = []
    dfs(s, [], 0, wSet, rslt)

    return rslt

def dfs(s, tl, start, wSet, rslt):
    n = len(s)
    if start == n:
        rslt.append(' '.join(tl))

    for end in range(start, n):
        if s[start:end+1] in wSet:
            tl.append(s[start:end+1])
            dfs(s, tl, end+1, wSet, rslt)
            tl.pop()

def wordBreakBFS(s, wList):
    """
    29/37 passed. TLE
    """
    wSet = set(wList)
    q = deque()
    q.append((0, ''))
    rslt = []

    while q:
        n = q.popleft()
        start = n[0]
        for end in range(start, len(s)):
            if s[start:end+1] in wSet:
                tl = n[1] + ' ' + s[start:end+1]
                if end == len(s)-1:
                    rslt.append(tl[1:])
                    break
                q.append((end+1, tl))
    return rslt

def wordBreak_dp(s, wList):
    """
    TLE 29/37
    """
    dp = [x[:] for x in [[]]*len(s)]
    wSet = set(wList)
    n = len(s)

    for start in reversed(range(n)):
        for end in range(start, n):
            if s[start:end+1] in wSet and end+1 == n:
                dp[start].append([s[start:end+1]])
            elif s[start:end+1] in wSet and dp[end+1]:
                for l in dp[end+1]:
                    dp[start].append([s[start:end+1]] + l)
    return [' '.join(l) for l in dp[0]]

def test1():
    s = 'catsanddog'
    wList = ['cat', 'cats', 'and', 'sand', 'dog']
    print(wordBreakSS(s, wList))
    print(wordBreak_dp(s, wList))
    print('--------------------')

def test2():
    s = 'abcedf'
    wList = ['a', 'b', 'c', 'd', 'e', 'f', 'abcedf']
    print(wordBreakSS(s, wList))
    print(wordBreak_dp(s, wList))
    print('--------------------')

if __name__ == '__main__':
    test1()
    test2()


