#!/usr/bin/python
"""
Given a 2d binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
leetcode #221.
"""

def maximal_square_dp(mtx):
    """
    Solving the problem using dynamic programming with O(mn) speed and O(mn) space.
    """
    # declare result matrix
    w = len(mtx[0])
    h = len(mtx)

    rslt = [x[:] for x in [[0] * (w+1)] * (h+1)]

    maxsqlen = 0

    for i in xrange(1, len(rslt)):
        for j in xrange(1, len(rslt[0])):
            if mtx[i-1][j-1] == 1:
                rslt[i][j] = min(rslt[i-1][j], rslt[i][j-1], rslt[i-1][j-1]) + 1

                maxsqlen = max(maxsqlen, rslt[i][j])

    return maxsqlen*maxsqlen

def maximal_square_dp_better_space(mtx):
    """
    Solving the problem using dynamic programming with O(mn) speed and O(n) space.
    """
    w = len(mtx[0])
    h = len(mtx)

    rslt = [0]*(w+1)

    maxsqlen = 0
    prev = 0
    for i in xrange(1, h+1):
        for j in xrange(1, w+1):
            tmp = rslt[j]
            if mtx[i-1][j-1] == 1:
                rslt[j] = min(rslt[j-1], rslt[j], prev) + 1
                maxsqlen = max(maxsqlen, rslt[j])
            else:
                rslt[j] = 0
            prev = tmp

    return maxsqlen*maxsqlen

def test1():
    mtx = [[1, 0, 1, 0, 0], \
           [1, 0, 1, 1, 1], \
           [1, 1, 1, 1, 1], \
           [1, 0, 0, 1, 0]]

    print(maximal_square_dp(mtx))
    print(maximal_square_dp_better_space(mtx))

def test2():
    mtx = [[1, 1, 1, 1], \
           [1, 1, 1, 1], \
           [1, 1, 0, 0], \
           [1, 1, 0, 1]]

    print(maximal_square_dp(mtx))
    print(maximal_square_dp_better_space(mtx))

def test3():
    mtx = [[1, 1, 0, 1], \
           [0, 0, 0, 1], \
           [0, 0, 0, 0], \
           [0, 0, 0, 1]]

    print(maximal_square_dp(mtx))
    print(maximal_square_dp_better_space(mtx))

def test4():
    mtx = [[0, 1, 1, 1, 0], \
           [1, 1, 1, 1, 0], \
           [0, 1, 1, 1, 1], \
           [0, 1, 1, 1, 1], \
           [0, 0, 1, 1, 1]]

    print(maximal_square_dp(mtx))
    print(maximal_square_dp_better_space(mtx))

if __name__ == '__main__':
    test1()
    print('------')
    test2()
    print('------')
    test3()
    print('------')
    test4()
