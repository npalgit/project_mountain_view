#!/usr/bin/python
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

#93
REDDO: know how to do maxHistogram first. Then just read over the solution. no need to code everything.
"""

def maxRectangle(mtx):
    if not mtx: return 0
    w, h = len(mtx[0]), len(mtx)
    max_rec = 0
    dp = [0]*(w+1)
    for row in range(h):
        max_rec = max(max_rec, processRow(mtx, row, dp))
    return max_rec

def processRow(mtx, row, dp):
    stck = [-1]
    max_area = 0
    for col in range(len(dp)):
        if col < len(dp)-1:
            if mtx[row][col] == '0': dp[col] = 0
            else: dp[col] += 1
        while dp[col] < dp[stck[-1]]:
            h = dp[stck.pop()]
            w = col - stck[-1]-1
            max_area = max(max_area, w*h)
        stck.append(col)
    return max_area

def test1():
    mtx = ["10100","10111","11111","10010"]
    print(maxRectangle(mtx))

if __name__ == '__main__':
    test1()
