#!/usr/bin/python
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0

leetcode #35
REDO: Do it in log(n) different binary search methods.
"""
def searchInsertPos1(l, k):
    beg, end = 0, len(l)-1

    while beg <= end:
        mid = beg + (end-beg)/2

        if l[mid] < k:
            beg = mid+1
        else:
            end = mid-1

    return beg

def searchInsertPos(l, k):
    beg, end = 0, len(l)
    while beg < end:
        mid = beg + (end-beg)/2

        if l[mid] < k:
            beg = mid+1
        else:
            end = mid

    return beg

def searchInsertPosLinear(l, k):
    for i, item in enumerate(l):
        if item >= k:
            return i

    return len(l)

def test1():
    l = [1, 3, 5, 6]
    print(searchInsertPos(l, 5))
    print(searchInsertPosLinear(l, 5))
    print("--------------")

def test2():
    l = [1, 3, 5, 6]
    print(searchInsertPos(l, 2))
    print(searchInsertPosLinear(l, 2))
    print("--------------")

def test3():
    l = [1, 3, 5, 6]
    print(searchInsertPos(l, 7))
    print(searchInsertPosLinear(l, 7))
    print("--------------")

def test4():
    l = [1, 3, 5, 6]
    print(searchInsertPos(l, 0))
    print(searchInsertPosLinear(l, 0))
    print("--------------")

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
