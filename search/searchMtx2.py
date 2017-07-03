#!/usr/bin/python
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
#240
REDDO: learn the trick
"""
def search(mtx, targ):
    row, col = 0, len(mtx[0])-1
    while col >= 0 and row < len(mtx):
        if mtx[row][col] == targ: return True
        elif mtx[row][col] > targ: col -= 1
        elif mtx[row][col] < targ: row += 1

    return False

def test1():
    mtx = [ \
        [1,   4,  7, 11, 15], \
        [2,   5,  8, 12, 19], \
        [3,   6,  9, 16, 22], \
        [10, 13, 14, 17, 24], \
        [18, 21, 23, 26, 30]]

    print(search(mtx, 8))
    print(search(mtx, 20))

if __name__ == '__main__':
    test1()
