#!/usr/bin/python
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

#268
"""
def missingNumberSort(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if i != nums[i]:
            break
        i += 1
    return i

def missingNumber(nums):
    """
    rely on summation formula
    """
    n = len(nums)
    total_sum = n*(1+n)/2.0

    partial_sum = 0
    for i in nums:
        partial_sum += i

    return total_sum-partial_sum

def test1():
    nums = [0, 1, 3]
    print(missingNumberSort(nums))
    print(missingNumber(nums))

def test2():
    nums = [0, 1, 2]
    print(missingNumberSort(nums))
    print(missingNumber(nums))

if __name__ == '__main__':
    test1()
    test2()
