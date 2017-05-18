#!/usr/bin/python
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

leetcode #53
"""
def maxSubarray(l):
    if not l:
        return None

    max_sub = l[0]
    max_overall = l[0]

    for i, item in enumerate(l[1:]):
        max_sub = max(item, max_sub+item)
        max_overall = max(max_overall, max_sub)

    return max_overall

def test1():
    l = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubarray(l))

def test2():
    l = [0, 0, 0, 0, 2, -1, 2]
    print(maxSubarray(l))

def test3():
    l = [1]
    print(maxSubarray(l))

def test4():
    l = [-2, 1]
    print(maxSubarray(l))

def test5():
    l = [-3, -2]
    print(maxSubarray(l))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
