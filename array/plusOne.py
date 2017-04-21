#!/usr/bin/python
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
#66
"""

def po(nums):
    """
    98% performance
    """
    idx = len(nums)-1

    while idx >= 0:
        r = nums[idx] + 1
        if r <= 9:
            nums[idx] = r
            return nums

        nums[idx] = r%10
        idx -= 1
    return [1] + nums

def test1():
   nums = [1, 2, 3, 4]
   print(po(nums))

def test2():
   nums = [9, 9, 9, 9]
   print(po(nums))

if __name__ == '__main__':
    test1()
    test2()
