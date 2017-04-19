#!/usr/bin/python
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#51
REDO: the backtrack solution.
"""
from collections import OrderedDict
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
