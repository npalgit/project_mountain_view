#!/usr/bin/python
"""
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn't exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

For example:
          20
        /   \
       9     25
     /  \
   5      12
         /  \
        10   14
For num = 17, return 14

from pramp
"""
from btNode import BTNode

def findSmallestBSTKey(n, targ):
    return dfs(n, targ, -1)

def dfs(n, targ, min_val):
    if not n: return min_val
    # branch left, when targ >= n.val
    if targ > n.val:
        min_val = n.val
        return dfs(n.right, targ, min_val)
    return dfs(n.left, targ, min_val)

def findSmallestBSTKey_itr(n, targ):
    min_val = -1
    while n:
        if targ > n.val:
            min_val = n.val
            n = n.right
        else:
            n = n.left
    return min_val

def test1():
    n20 = BTNode(20)
    n9  = BTNode(9)
    n25 = BTNode(25)
    n5  = BTNode(5)
    n12 = BTNode(12)
    n10 = BTNode(10)
    n14 = BTNode(14)

    n20.left = n9
    n20.right = n25
    n9.left = n5
    n9.right = n12
    n12.left = n10
    n12.right = n14

    print(findSmallestBSTKey_itr(n20, 17))
    print(findSmallestBSTKey(n20, 17))
    print(findSmallestBSTKey_itr(n20, 12))
    print(findSmallestBSTKey(n20, 12))
    print(findSmallestBSTKey_itr(n20, 14))
    print(findSmallestBSTKey(n20, 14))

if __name__ == '__main__':
    test1()
