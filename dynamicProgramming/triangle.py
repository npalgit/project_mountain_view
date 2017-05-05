#!/usr/bin/python
"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.

#120
"""

def triangle(tri):
    """
    got this first try. 81.92% performance. only thing was misunderstanding the question.
    you can only go down and down-right. I thought you could still go down-left.
    You could also modify the orignal triangle
    """
    n = len(tri[-1])
    rslt = [[0]*n, [0]*n]
    int_max = 0x7fffffff
    w_idx, r_idx = 0, 0
    rslt[0][0] = tri[0][0]

    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            w_idx = i%2
            r_idx = w_idx^1
            lhs = rslt[r_idx][j-1] if j-1 >= 0 else int_max
            mid = rslt[r_idx][j] if j < len(tri[i-1]) else int_max

            rslt[w_idx][j] = min(lhs, mid) + tri[i][j]

    return min(rslt[w_idx])

def test1():
    tri = [ \
        [2], \
        [3,4], \
        [6,5,7], \
        [4,1,8,3]]
    print(triangle(tri))

def test2():
    tri = [[-1],[3,2],[-3,1,-1]]
    print(triangle(tri))

if __name__ == '__main__':
    test1()
    test2()
