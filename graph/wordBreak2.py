#!/usr/bin/python
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

def wordBreakBT(s, wList):
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

def wordBreak(s, wList):
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

def wordBreakBTMem(s, wList):
    """
    Here for historical reference. There are duplicated answers at the end
    """
    wSet = set(wList)
    mem = {}
    dfsMem(s, 0, wSet, mem)
    #print(mem)
    return [' '.join(l) for l in mem[len(s)-1]]

def dfsMem(s, start, wSet, mem):
    n = len(s)
    for end in range(start, n):
        if s[start:end+1] in wSet:
            prev_ls = mem.get(start-1, [[]])
            new_ls = copy.deepcopy(prev_ls)
            for l in new_ls:
                l.append(s[start:end+1])
            end_ls = mem.get(end, [])
            end_ls.extend(new_ls)
            mem[end] = end_ls
            print(mem)
            dfsMem(s, end+1, wSet, mem)

def test1():
    s = 'catsanddog'
    wList = ['cat', 'cats', 'and', 'sand', 'dog']
    #print(wordBreak(s, wList))
    print(wordBreakSS(s, wList))
    #print(wordBreakBT(s, wList))

def test2():
    s = 'abcedf'
    wList = ['a', 'b', 'c', 'd', 'e', 'f', 'abcedf']
    #print(wordBreak(s, wList))
    print(wordBreakSS(s, wList))
    #print(wordBreakBT(s, wList))

if __name__ == '__main__':
    test1()
    test2()


"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
#140
REDO: dfs_mem, bfs_mem, time complexity
"""
