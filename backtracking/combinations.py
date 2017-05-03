#!/usr/bin/python
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

#77
Note: python backtracking TLE
REDO: this as a series of backtracking
"""
def combo(n, k):
    nums = [i for i in range(1, n+1)]
    rslt = []
    dfs(rslt, 0, nums, n, k, [])
    return rslt

def dfs(rslt, start, nums, n, k, l):
    if len(l) == k:
        rslt.append(l[:])
        return

    for i in range(start, n):
        l.append(nums[i])
        dfs(rslt, i+1, n, k, l)
        l.pop()

def combo2(n, k):
    rslt = []
    dfs2(rslt, 1, n, k, [])
    return rslt

def dfs2(rslt, start, n, k, l):
    if k == 0:
        rslt.append(l[:])
        return

    for i in range(start, n+1):
        l.append(i)
        dfs2(rslt, i+1, n, k-1, l)
        l.pop()

def test1():
   print(combo2(4, 2))

def test2():
   print(combo2(20, 16))

if __name__ == '__main__':
    test1()
    test2()
