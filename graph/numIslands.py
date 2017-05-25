#!/usr/bin/python
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

#200
"""

def countIslnds(grid):
    if not grid: return 0
    count = 0
    w, h = len(grid[0]), len(grid)
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count

def dfs(grid, i, j):
    w, h = len(grid[0]), len(grid)
    if i < 0 or j < 0 or i >= h or j >= w or grid[i][j] != '1': return
    grid[i][j] = '0'
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)

def test1():
    inp = ['11000', '11000', '00100', '00011']
    grid = [list(x) for x in inp]
    print(countIslnds(grid))

if __name__ == '__main__':
    test1()
