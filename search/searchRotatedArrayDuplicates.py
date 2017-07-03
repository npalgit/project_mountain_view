#!/usr/bin/python
"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

#81
REDDO: need to figure out the sol on your own this along with #33
"""

def searchInSorted2ndBest(nums, targ):
    if not nums: return False
    beg, end = 0, len(nums)-1

    while beg < end:
        mid = beg + (end-beg)/2
        if targ == nums[mid]: return True
        # or: while beg < end and nums[beg] == nums[end]:
        if nums[beg] == nums[mid] and nums[mid] == nums[end]:
            beg += 1
            end -=1
        elif nums[beg] <= nums[mid]:
            if nums[beg] <= targ and targ < nums[mid]:
                end = mid - 1
            else:
                beg = mid + 1
        else:
            if nums[mid] < targ and targ <= nums[end]:
                beg = mid + 1
            else:
                end = mid-1

    return True if nums[beg] == targ else False

def test1():
    nums = [5, 6, 1, 2, 2, 3, 4, 5, 5]
    print(searchInSorted2ndBest(nums, 9))

def test2():
    nums = [1, 3, 1, 1, 1, 1]
    print(searchInSorted2ndBest(nums, 3))

if __name__ == '__main__':
    test1()
    test2()
