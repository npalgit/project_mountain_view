#!/usr/bin/python
"""
Given a 2d binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
leetcode #221. This particular solution takes in array of string, which is for the submission
on leetcode.
"""

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
            if mtx[i-1][j-1] == '1':
                rslt[j] = min(rslt[j-1], rslt[j], prev) + 1
                maxsqlen = max(maxsqlen, rslt[j])
            else:
                rslt[j] = 0
            prev = tmp

    return maxsqlen*maxsqlen

def test1():
    mtx = ['10100', \
           '10111', \
           '11111', \
           '10010']

    print(maximal_square_dp_better_space(mtx))

def test2():
    mtx = ['1111', \
           '1111', \
           '1100', \
           '1101']

    print(maximal_square_dp_better_space(mtx))

def test3():
    mtx = ['1101', \
           '0001', \
           '0000', \
           '0001']

    print(maximal_square_dp_better_space(mtx))

def test4():
    mtx = ['01110', \
           '11110', \
           '01111', \
           '01111', \
           '00111']

    print(maximal_square_dp_better_space(mtx))

if __name__ == '__main__':
    test1()
    print('------')
    test4()
#    test2()
#    print('------')
#    test3()
#    print('------')
#   test4()
