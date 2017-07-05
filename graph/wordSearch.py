#!/usr/bin/python
"""
#79
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
  ] 

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
] 
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

#79
REDDO: need to figure out the correct approach first
"""
from collections import deque

def wSearchDfs(mtx, w):
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if dfs((i, j), w, set(), mtx):
                return True

    return False

def dfs(n, s, trace, mtx):
    if not s: return True
    i, j = n[0], n[1]
    if n in trace or \
       i< 0 or i >= len(mtx) or \
       j < 0 or j >= len(mtx[0]) or \
       mtx[i][j] != s[0]: return False

    trace.add(n)
    rslt = dfs((i-1, j), s[1:], trace, mtx) or \
            dfs((i+1, j), s[1:], trace, mtx) or \
            dfs((i, j-1), s[1:], trace, mtx) or \
            dfs((i, j+1), s[1:], trace, mtx)
    trace.remove(n)
    return rslt

def wSearchDfsBetterMem(mtx, w):
    mtx = map(list, mtx)
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if dfsBetterMem((i, j), w, mtx):
                return True

    return False

def dfsBetterMem(n, s, mtx):
    if not s: return True
    i, j = n[0], n[1]
    if i< 0 or i >= len(mtx) or \
       j < 0 or j >= len(mtx[0]) or \
       mtx[i][j] != s[0]: return False

    tmp, mtx[i][j] = mtx[i][j], -1
    rslt = dfsBetterMem((i-1, j), s[1:], mtx) or \
            dfsBetterMem((i+1, j), s[1:], mtx) or \
            dfsBetterMem((i, j-1), s[1:], mtx) or \
            dfsBetterMem((i, j+1), s[1:], mtx)
    mtx[i][j] = tmp

    return rslt

def wSearch2(mtx, w):
    """
    Note: bfs not the best solution. I assumed the order does not matter. but it matters
    """
    if mtx is None or w is None: return False

    nrows, ncols = len(mtx), len(mtx[0])

    for i in range(nrows):
        for j in range(ncols):
            s = {}
            trace = set()
            for itm in w:
                if itm not in s: s[itm] = 1
                else: s[itm] += 1

            if bfs2(mtx, i, j, s, trace): return True

    return False

def bfs2(mtx, i, j, s, trace):
    q = deque()
    nrows, ncols = len(mtx), len(mtx[0])
    if mtx[i][j] in s:
        v = mtx[i][j]
        s[v] -= 1
        if s[v] == 0: del s[v]
        if not s: return True
        q.append((i, j))
        trace.add((i, j))

    while q:
        n = q.popleft()

        for nbr in getNbr2(n[0], n[1], nrows, ncols):
            v = mtx[nbr[0]][nbr[1]]
            if v in s and nbr not in trace:
                s[v] -= 1
                if s[v] == 0: del s[v]
                if not s: return True
                trace.add(nbr)
                q.append(nbr)
    return False

def getNbr2(i, j, nrows, ncols):
    rslt = []
    if j-1 >= 0 and (i, j-1): rslt.append((i, j-1))
    if j+1 < ncols and (i, j+1): rslt.append((i, j+1))
    if i+1 < nrows and (i+1, j): rslt.append((i+1, j))
    if i-1 >= 0 and (i-1, j): rslt.append((i-1, j))

    return rslt

def wSearch(mtx, w):
    """
    BFS is not the best choice because I assumed the order did not matter, but it matters.
    Use a string instead of a set. TODO: verify works same as using a set,
    with the current test case looks like it works the same. 78/87 leetcode passed.
    Same as wSearch2 using a set
    """
    if mtx is None or w is None: return False

    nrows, ncols = len(mtx), len(mtx[0])

    for i in range(nrows):
        for j in range(ncols):
            s = w
            trace = set()
            if bfs(mtx, i, j, s, trace): return True

    return False

def bfs(mtx, i, j, s, trace):
    q = deque()
    nrows, ncols = len(mtx), len(mtx[0])
    if mtx[i][j] == s[0]:
        s = s[1:]
        if not s: return True
        q.append((i, j))
        trace.add((i, j))

    while q:
        n = q.popleft()

        for nbr in getNbr(n[0], n[1], nrows, ncols):
            v = mtx[nbr[0]][nbr[1]]
            if v == s[0] and nbr not in trace:
                s = s[1:]
                if not s: return True
                trace.add(nbr)
                q.append(nbr)
    return False

def getNbr(i, j, nrows, ncols):
    rslt = []
    if j-1 >= 0 and (i, j-1): rslt.append((i, j-1))
    if j+1 < ncols and (i, j+1): rslt.append((i, j+1))
    if i+1 < nrows and (i+1, j): rslt.append((i+1, j))
    if i-1 >= 0 and (i-1, j): rslt.append((i-1, j))

    return rslt

# -------------- re-implement dfs ---------------------
def wSearchDfs_r(mtx, w):
    mtx = map(list, mtx)
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if dfs_r((i, j), w, mtx):
                return True
    return False

def dfs_r(n, s, mtx):
    if not s: return True
    i, j = n[0], n[1]
    if i < 0 or j < 0 or i >= len(mtx) or j >= len(mtx[0]) or mtx[i][j] != s[0]:
        return False

    sub_s = s[1:]
    tmp, mtx[i][j] = mtx[i][j], -1

    if dfs_r((i-1, j), sub_s, mtx) or \
        dfs_r((i+1, j), sub_s, mtx) or \
        dfs_r((i, j-1), sub_s, mtx) or \
        dfs_r((i, j+1), sub_s, mtx):
        return True

    mtx[i][j] = tmp
    return False
# ------------- end re-implement -------------------

def test1():
   mtx = [['A', 'B', 'C', 'E'], \
         ['S', 'F', 'C', 'S'], \
          ['A', 'D', 'E', 'E']]
   w = 'ABCCED'
   print(wSearchDfsBetterMem(mtx, w))
   print(wSearchDfs_r(mtx, w))
   print('------------------')

def test2():
   mtx = [['A', 'B', 'C', 'E'], \
         ['S', 'F', 'C', 'S'], \
          ['A', 'D', 'E', 'E']]
   w = 'SEE'
   print(wSearchDfsBetterMem(mtx, w))
   print(wSearchDfs_r(mtx, w))
   print('------------------')

def test3():
   mtx = [['A', 'B', 'C', 'E'], \
         ['S', 'F', 'C', 'S'], \
          ['A', 'D', 'E', 'E']]
   w = 'ABCB'
   print(wSearchDfsBetterMem(mtx, w))
   print(wSearchDfs_r(mtx, w))
   print('------------------')

def test4():
    mtx = ["abc","aed","afg"]
    w = "abcdef"
    print(wSearchDfsBetterMem(mtx, w))
    print(wSearchDfs_r(mtx, w))
    print('------------------')

def test5():
    mtx = ["CAA","AAA","BCD"]
    w = "AAB"
    print(wSearchDfsBetterMem(mtx, w))
    print(wSearchDfs_r(mtx, w))
    print('------------------')

def test6():
    mtx = ["ab","cd"]
    w = "abcd"
    print(wSearchDfsBetterMem(mtx, w))
    print(wSearchDfs_r(mtx, w))
    print('------------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
