#!/usr/bin/python
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
leetcode #1
"""
def twoSum(arr, targ):
    dic = {}
    for i in xrange(len(arr)):
        if arr[i] not in dic:
            dic[targ - arr[i]] = i
        else:
            return (dic[arr[i]], i)

    return None

def test1():
    arr = [2, 7, 11, 15]
    print(twoSum(arr, 9))

if __name__ == '__main__':
    test1()
