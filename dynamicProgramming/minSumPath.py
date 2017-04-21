#!/usr/bin/python
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
#64
"""
def mps(grid):
    """
    69% performance
    """
    int_max = 0x7fffffff
    m, n = len(grid[0]), len(grid)
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            t = int_max if i-1 < 0 else grid[i-1][j]
            l = int_max if j-1 < 0 else grid[i][j-1]
            grid[i][j] = min(t, l)+grid[i][j]
    
    return grid[-1][-1]

def test1():
    grid = [ \
        [1,2,0], \
        [5,1,0], \
        [0,6,0]]

    print(mps(grid))

if __name__ == '__main__':
    test1()
