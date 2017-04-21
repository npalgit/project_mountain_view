#!/usr/bin/python
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#62
"""
def uniquePaths(m, n):
    rslt = [x[:] for x in [[0]*(m+1)]*(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: 
                rslt[1][1] = 1
            else:
                rslt[i][j] = rslt[i-1][j] + rslt[i][j-1]

    return rslt[-1][-1]

def test1():
    print(uniquePaths(4, 3))

if __name__ == '__main__':
    test1()
