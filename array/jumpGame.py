#!/usr/bin/python
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

leetcode #55
REDO: maybe not top priority, its like the max subarray problem. Do it without looking at the solution.
"""
def jumpG(l):
    max_idx = 0
    for i, item in enumerate(l):
        if max_idx < i:
            return False

        max_idx = max(max_idx, i + item)

    return True

def test1():
    l = [2, 3, 1, 1, 4]
    print(jumpG(l))

def test2():
    l = [3, 2, 1, 0, 4]
    print(jumpG(l))

if __name__ == "__main__":
    test1()
    test2()
