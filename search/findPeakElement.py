#!/usr/bin/python
"""
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -oo

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#162
#REDO: this and all similar bin search problem
"""
def findPeak(nums):
    beg, end = 0, len(nums)-1

    while beg < end-1:
        mid = beg+(end-beg)/2
        if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
            return mid

        if nums[mid+1] > nums[mid]:
            beg = mid+1
        else:
            end = mid-1

    return beg if nums[beg] > nums[end] else end

def findPeak2(nums):
    beg, end = 0, len(nums)-1

    while beg < end:
        mid = beg+(end-beg)/2
        if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
            return mid

        if nums[mid+1] > nums[mid]:
            beg = mid+1
        else:
            end = mid-1

    return beg

def test1():
    nums = [0, 1, 2, 3]
    print(findPeak(nums))
    print(findPeak2(nums))
    print('------------------')

def test2():
    nums = [3, 2, 1, 0]
    print(findPeak(nums))
    print(findPeak2(nums))
    print('------------------')

def test3():
    nums = [1,6,5,4,3,2,1]
    print(findPeak(nums))
    print(findPeak2(nums))
    print('------------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
