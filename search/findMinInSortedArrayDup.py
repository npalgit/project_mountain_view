#!/usr/bin/python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
#154
REDDO
"""
def findMinInRotatedDup(nums):
    beg, end = 0, len(nums)-1

    while beg < end:
        while end >= beg and nums[beg] == nums[end]:
            end -= 1

        if nums[beg] < nums[end]: return nums[beg]

        mid = beg + (end-beg)/2
        if nums[mid] >= nums[beg]:
            beg = mid+1
        else:
            end = mid

    return nums[beg]

def test1():
    nums = [4, 4, 4, 4, 0, 1, 2]
    print(findMinInRotatedDup(nums))

def test2():
    nums = [1, 1]
    print(findMinInRotatedDup(nums))

if __name__ == '__main__':
    test1()
    test2()
