#!/usr/bin/python
"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""
from btNode import BTNode

def constructTree(arr):
    if not arr: return None

    idx = findMax(arr)
    n = BTNode(arr[idx])
    lhs = constructTree(arr[:idx])
    rhs = constructTree(arr[idx+1:])
    n.left = lhs
    n.right = rhs

    return n

def findMax(arr):
    max_idx = -1
    max_val = -0x7fffffff-1
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_idx

def test1():
    arr = [3,2,1,6,0,5]
    BTNode.print_nodes(constructTree(arr))

if __name__ == '__main__':
    test1()
