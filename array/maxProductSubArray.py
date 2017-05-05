#!/usr/bin/python
"""
Find the contiguous subarray within an array (containing at least one number) which has
the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

#152
REDO
"""

def maxProdSubarray(nums):
    if not nums: return 0

    max_here = 0
    min_here = nums[0]
    max_overall = nums[0]
    max_prev = nums[0]

    for i in nums[1:]:
        max_here = max(max(min_here*i, max_prev*i), i)
        min_here = min(min(min_here*i, max_prev*i), i)
        max_overall = max(max_here, max_overall)
        max_prev = max_here

    return max_overall

def test1():
    nums = [2, 3, -2, 4]
    print(maxProdSubarray(nums))

def test2():
    nums = [-2, -3, -2, -4]
    print(maxProdSubarray(nums))

if __name__ == '__main__':
    test1()
    test2()
