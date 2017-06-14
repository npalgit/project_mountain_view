#!/usr/bin/python
"""
After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police
#213
"""
def hrc(nums):
    """
    Got it first try
    """
    if len(nums) == 1: return nums[0]
    n = len(nums)-1
    return max(rob(nums, 0, n-1), rob(nums, 1, n))

def rob(nums, b, e):
    prevm0 = 0
    prevm1 = 0
    curr = 0
    for i in range(b, e+1):
        temp = max(prevm0, prevm1) + nums[i]
        prevm1 = prevm0
        prevm0 = curr
        curr = temp

    return max(prevm0, curr)

def test1():
    nums = [9, 1, 3, 5, 8, 11, 3]
    print(hrc(nums))

if __name__ == '__main__':
    test1()
