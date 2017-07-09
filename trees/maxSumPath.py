#!/usr/bin/python
"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

#124
REDDO: tricky question with clear algorithm. This is a hard question
"""
from btNode import BTNode

def maxSumPath(n):
    max_val = [-0x7fffffff-1]
    maxSumHelper(n, max_val)
    return max_val[0]

def maxSumHelper(n, max_val):
    if not n: return 0
    left = max(0, maxSumHelper(n.left, max_val))
    right = max(0, maxSumHelper(n.right, max_val))

    max_val[0] = max(max_val[0], left+right+n.val)

    return max(left, right) + n.val

def test1():
    nm1 = BTNode(-1)
    nm2 = BTNode(-2)
    nm3 = BTNode(-3)
    nm4 = BTNode(-4)
    nm5 = BTNode(-5)
    nm6 = BTNode(-6)
    n12 = BTNode(12)
    n15 = BTNode(15)

    nm1.left = nm2
    nm1.right = n12
    nm2.right = nm5
    n12.right = nm4
    nm4.left = n15
    nm4.right = nm2
    nm2.left = nm6

    print(maxSumPath(nm1))

if __name__ == '__main__':
    test1()
