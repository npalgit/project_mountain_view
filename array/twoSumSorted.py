#!/usr/bin/python
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

#167
"""
def twoSum(nums, targ):
    beg, end = 0, len(nums)-1

    while beg < end:
        if nums[beg] + nums[end] == targ:
            return [beg+1, end+1]
        elif nums[beg] + nums[end] < targ:
            beg += 1
        else:
            end -= 1

    return [-1, -1]

def test1():
    nums = [2, 7, 11, 15]
    print(twoSum(nums, 9))

if __name__ == '__main__':
    test1()
