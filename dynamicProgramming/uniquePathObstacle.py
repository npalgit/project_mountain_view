#!/usr/bin/python
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
#63
"""
def upo(grid):
    if grid[0][0] == 1: return 0
    grid[0][0] = 1

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue

            if grid[i][j] == 1:
                grid[i][j] = 0
                continue
            t = 0 if i-1 < 0 else grid[i-1][j]
            l = 0 if j-1 < 0 else grid[i][j-1]
            grid[i][j] = t + l

    return grid[-1][-1]

def test1():
    grid = [ \
        [0,0,0], \
        [0,1,0], \
        [0,0,0]]

    print(upo(grid))

if __name__ == '__main__':
    test1()
