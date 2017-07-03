#!/usr/bin/python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

#153
REDDO: need to figure this out fast with no hint
"""
def findMin(nums):
    beg, end = 0, len(nums)-1
    while beg < end:
        if nums[beg] < nums[end]: return nums[beg]

        mid = beg + (end-beg)/2

        if nums[beg] <= nums[mid]:
            beg = mid +1
        else:
            end = mid

    return nums[beg]

def findMin_r(nums):
    beg, end = 0, len(nums)-1
    if nums[beg] < nums[end]: return nums[beg]
    while beg < end:
        mid = beg + (end-beg)/2

        if nums[0] > nums[mid]:
            end = mid
        else:
            beg = mid+1

    return nums[beg]

def test1():
    print(findMin([6, 7, 0, 1, 2, 3, 4, 5]))

if __name__ == '__main__':
    test1()
