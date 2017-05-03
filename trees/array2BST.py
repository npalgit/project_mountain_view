#!/usr/bin/python
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#108
"""
from btNode import BTNode

def a2t(nums):
    if not nums: return None
    beg, end = 0, len(nums)
    mid = beg + (end-beg)/2
    n = BTNode(nums[mid])
    n.left = a2t(nums[:mid])
    n.right = a2t(nums[mid+1:])
    return n

def test1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    BTNode.print_nodes(a2t(nums))

if __name__ == '__main__':
    test1()
