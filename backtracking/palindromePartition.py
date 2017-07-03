#!/usr/bin/python
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
#131
REDDO: go over all the backtracking problems
"""
def palinPart(s):
    """
    34% - 66.74% speed. 
    """
    lists = []
    dfs(lists, [], s, 0)
    return lists

def dfs(lists, l, s, start):
    if start == len(s):
        lists.append(list(l))
        return

    for i in range(start, len(s)):
        if not isPalin(s[start:i+1]): continue
        l.append(s[start:i+1])
        dfs(lists, l, s, i+1)
        l.pop()

def palinPart_r(s):
    res = []
    trace = []
    dfs_r(s, 0, trace, res)
    return res

def dfs_r(s, i, trace, res):

    if i == len(s):
        res.append(list(trace))
        return

    for h in range(i, len(s)):
        l = i
        if isPalin(s[l:h+1]):
            trace.append(s[l:h+1])
            dfs_r(s, h+1, trace, res)
            trace.pop()

def isPalinOneLiner(s):
    """
    Alternative implementation of is palin for reference only
    """
    return s == s[::-1]

def isPalin(s):
    beg = 0
    end = len(s)-1
    while beg <= end:
        if s[beg] != s[end]: return False
        beg += 1
        end -= 1

    return True

def test1():
    s = 'aab'
    print(palinPart(s))
    print(palinPart_r(s))
    print('--------------')

def test2():
    s = 'aaab'
    print(palinPart(s))
    print(palinPart_r(s))
    print('--------------')

def test3():
    s = 'aabaac'
    print(palinPart(s))
    print(palinPart_r(s))
    print('--------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
