#!/usr/bin/python
"""
Given an array of size n, find the majority element. The majority element is the element
that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

#169
REDO: moore's majority algo
review: moore's majority algo
"""

def majority(nums):
    """
    Moore's majority algorithm.
    """
    majority, count = nums[0], 1

    for i in nums[1:]:
        if count == 0:
            majority = i
            count += 1
        elif i == majority:
            count += 1
        else:
            count -= 1

    return majority

def majorityOneLiner(nums):
    """
    After sort, the middle will always be a majority element.
    """
    return sorted(nums)[len(nums)/2]

def test1():
    nums = [3, 3, 0, 3, 1, 2, 3]
    print(majority(nums))
    print(majorityOneLiner(nums))

if __name__ == '__main__':
    test1()


