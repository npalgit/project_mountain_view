#!/usr/bin/python
"""
write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

#74
"""

def search2D(mtx, targ):
    if not mtx or targ is None: return False
    nrows = len(mtx)
    ncols = len(mtx[0])
    beg, end = 0, nrows*ncols-1

    while beg <= end:
        mid = beg + (end-beg)/2
        num = mtx[mid/ncols][mid%ncols]
        if num == targ:
            return True
        elif num < targ:
            beg = mid+1
        else:
            end = mid-1
    return False

def test1():
    mtx = [ \
         [1,   3,  5,  7], \
         [10, 11, 16, 20], \
         [23, 30, 34, 50]]

    print(search2D(mtx, 3))

def test2():
    mtx = [ \
         [1,   3,  5,  7], \
         [10, 11, 16, 20], \
         [23, 30, 34, 50]]

    print(search2D(mtx, 6))

def test3():
    mtx = []
    print(search2D(mtx, 3))

if __name__ == '__main__':
    test1()
    test2()
    test3()
