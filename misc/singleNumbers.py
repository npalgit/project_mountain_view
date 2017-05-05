#!/usr/bin/python
"""
Given an array of integers, every element appears twice except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

#136
"""
def findSingleNum(nums):
    """
    Figured out first try, 94% performance.
    """
    rslt = 0
    for i in nums: rslt ^= i
    return rslt

def test1():
    nums = [4, 3, 3, 4, 9, 1, 12, 9, 1]
    print(findSingleNum(nums))

if __name__ == '__main__':
    test1()
