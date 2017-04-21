#!/usr/bin/python
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Count the number of solutions. Note this is nearly identical to #51
#52
"""
def nqns(n):
    """
    uses list representation. Good perfomance 83%
    """
    count = [0]

    dfs([], [], [], n, count)
    return count[0]


def dfs(qs, xy_diff, xy_sum, n, count):
    p = len(qs)
    if p == n:
        count[0] += 1
        return

    for q in range(n):
        if q not in qs and (p-q) not in xy_diff and (p+q) not in xy_sum:
            dfs(qs+[q], xy_diff+[p-q], xy_sum+[p+q], n, count)



def test1():
   print(nqns(8))

if __name__ == '__main__':
    test1()
