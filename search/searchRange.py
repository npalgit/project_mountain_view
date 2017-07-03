#!/usr/bin/python
"""
Given an array of integers sorted in ascending order, find the starting and ending position of
a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

leetcode#34
REDDO: this is based on insert pos. good question
"""
def searchRange(l, k):
    def search(l, k):
        beg, end = 0, len(l)
        while beg < end:
            mid = beg+(end-beg)/2

            if l[mid] < k:
                beg = mid+1
            else:
                end = mid

        return beg

    beg = search(l, k)
    
    # both return statements work below, slice the list a smart work around out of bound index.
    #return [beg, search(l, k+1)-1] if k in l[beg:beg+1] else [-1, -1]
    return [beg, search(l, k+1)-1] if beg < len(l) and k == l[beg] else [-1, -1]

def test1():
    l = [5, 7, 7, 8, 8, 10]
    print(searchRange(l, 8))

def test2():
    l = [5, 7, 7, 8, 8, 10, 10]
    print(searchRange(l, 10))

def test3():
    l = [5, 7, 7, 8, 8, 10]
    print(searchRange(l, 9))

def test4():
    l = [5, 7, 7, 8, 8, 10]
    print(searchRange(l, 5))

def test5():
    l = []
    print(searchRange(l, 3))

def test6():
    l = [2, 2]
    print(searchRange(l, 3))

def test7():
    l = [-1]
    print(searchRange(l, 0))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
