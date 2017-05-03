#!/usr/bin/python
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]113
"""
from btNode import BTNode

def pathSum(n, targ):
    """
    accepted first try 66.6% - 87.90% performance
    """
    ml = []
    pathSumHelper(n, ml, [], 0, targ)
    return ml

def pathSumHelper(n, ml, l, s, targ):
    if not n: return

    s += n.val
    l.append(n.val)

    if not n.left and not n.right and s == targ:
        ml.append(list(l))
        l.pop()
        return

    pathSumHelper(n.left, ml, l, s, targ)
    pathSumHelper(n.right, ml, l, s, targ)

    l.pop()

def test1():
    n5a  = BTNode(5)
    n4a  = BTNode(4)
    n8  = BTNode(8)
    n11 = BTNode(11)
    n7  = BTNode(7)
    n2  = BTNode(2)
    n13 = BTNode(13)
    n4b  = BTNode(4)
    n5b  = BTNode(5)
    n1  = BTNode(1)

    n5a.left = n4a
    n4a.left = n11
    n11.left = n7
    n11.right = n2
    n5a.right = n8
    n8.left = n13
    n8.right = n4b
    n4b.left = n5b
    n4b.right = n1

    print(pathSum(n5a, 22))

if __name__ == '__main__':
    test1()
