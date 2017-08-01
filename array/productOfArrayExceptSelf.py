#!/usr/bin/python
"""
Given an array of n integers where n > 1, nums, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the
purpose of space complexity analysis.)
#238
"""

def productExceptSelf(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    res = [1]*len(nums)

    prev = 1
    for i in range(len(nums)):
        left[i] = nums[i]*prev
        prev = left[i]
    prev = 1
    for i in reversed(range(len(nums))):
        right[i] = nums[i]*prev
        prev = right[i]

    for i in range(len(nums)):
        l_val = left[i-1] if i > 0 else 1
        r_val = right[i+1] if i < len(nums)-1 else 1
        res[i] = l_val*r_val

    return res

def productExceptSelfLessSpace(nums):
    len_n = len(nums)
    res = [1]*len_n
    prev = 1
    for i in range(len_n):
        res[i] = prev*nums[i]
        prev = res[i]

    prev = 1
    for i in reversed(range(len_n)):
        res[i] = res[i-1]*prev if i > 0 else prev
        prev = prev*nums[i]

    return res

def test1():
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
    print(productExceptSelfLessSpace(nums))

def test2():
    nums = [0, 0]
    print(productExceptSelf(nums))
    print(productExceptSelfLessSpace(nums))

if __name__ == '__main__':
    test1()
    test2()
