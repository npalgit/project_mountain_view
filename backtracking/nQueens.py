#!/usr/bin/python
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#51
REDDO: the backtrack solution.
"""
from collections import OrderedDict

def solveNQueens_r(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    res = []
    trace = []
    xy_sum = set()
    xy_diff = set()
    dfs_r(xy_sum, xy_diff, trace, res, n)

    return [['.'*el + 'Q' +'.'*(n-el-1) for el in sol] for sol in res]

def on_path(xy_sum, xy_diff, x, y):
    if y-x in xy_diff or x+y in xy_sum:
        return True

    return False

def dfs_r(xy_sum, xy_diff, trace, res, n):
    if len(trace) == n:
        res.append(list(trace))
        return

    for x in range(n):
        y = len(trace)+1
        if x in trace or on_path(xy_sum, xy_diff, x, y): continue

        xy_sum.add(x+y)
        xy_diff.add(y-x)
        trace.append(x)
        dfs_r(xy_sum, xy_diff, trace, res, n)
        trace.pop()
        xy_sum.remove(x+y)
        xy_diff.remove(y-x)

def nQs(n):
    """
    Using OrderedDict is acutally much slower than pure list. This yields 9%
    """
    result = []
    qs = OrderedDict()
    dfs(qs, set(), set(), n, result)
    return [['.'*i + 'Q'+ '.'*(n-i-1) for i in sol.keys()] for sol in result]

def dfs(qs, xy_diff, xy_sum, n, result):
    p = len(qs)
    if p == n:
        result.append(qs)
        return
    for q in range(n):
        if q not in qs and (p-q) not in xy_diff and (p+q) not in xy_sum:
            new_qs = OrderedDict(qs)
            new_qs[q] = None

            new_xy_diff = set(xy_diff)
            new_xy_diff.add(p-q)

            new_xy_sum = set(xy_sum)
            new_xy_sum.add(p+q)
            dfs(new_qs, new_xy_diff, new_xy_sum, n, result)

def nQs2(n):
    """
    uses list representation. Good perfomance 83%
    """
    result = []
    dfs2([], [], [], n, result)
    return [['.'*i + 'Q'+ '.'*(n-i-1) for i in sol] for sol in result]

def dfs2(qs, xy_diff, xy_sum, n, result):
    p = len(qs)
    if p == n:
        result.append(qs)
        return
    for q in range(n):
        if q not in qs and (p-q) not in xy_diff and (p+q) not in xy_sum:
            dfs2(qs+[q], xy_diff +[p-q], xy_sum+[p+q], n, result)

def test1():
    n = 4
    r = nQs(n)
    for s in r:
        print(r)
    print('--------')
    r = nQs2(n)
    for s in r:
        print(r)

if __name__ == '__main__':
    test1()
