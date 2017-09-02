#!/usr/bin/python
"""
Increasing Triplet Subsequence
#334
"""

def increasingTripSubseq(nums):
    i = 0
    for j in range(nums):
        if nums[j] > nums[i]:
            nums[i+1] = nums[j]
            i += 1

def binSearch(nums, b, e, k):
    while b < e:
        mid = b+(e-b)/2
        if k <= nums[mid]:
            e = mid
        else:
            b = mid+1
    return b

def test1():
    pass

if __name__ == '__main__':
    test1()
