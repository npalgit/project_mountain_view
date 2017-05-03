#!/usr/bin/python
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
#118
"""

def pascalT(n):
    if n == 0: return []
    if n == 1: return [[1]]
    if n == 2: return [[1], [1,1]]
    rslt = [[1], [1, 1]]
    pt(n-2, rslt)

    return rslt

def pt(n, rslt):
    if n == 0: return
    l = [1]
    prev_l = rslt[-1]
    for i in range(1, len(prev_l)):
        l.append(prev_l[i-1]+prev_l[i])
    l.append(1)
    rslt.append(l)
    pt(n-1, rslt)

def test1():
    print(pascalT(4))

def test2():
    print(pascalT(6))

if __name__ == '__main__':
    test1()
    test2()
