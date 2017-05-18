#!/usr/bin/python
"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
#70
"""
def climbStairs(n):
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    rslt = [1, 2]

    for i in range(2, n):
        s = rslt[0] + rslt[1]
        rslt[0], rslt[1] = rslt[1], s

    return rslt[-1]


def test1():
   print(climbStairs(7))

if __name__ == '__main__':
    test1()
