#!/usr/bin/python
"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
#285
"""
from btNode import BTNode

def inorderBSTSuccessor(root, p):
    succ = root
    n = root
    while n:
        if n.val <= p.val:
            n = n.right
        else:
            succ = n
            n = n.left

    return succ if succ.val > p.val else None

def test1():
    n11 = BTNode(11)
    n8  = BTNode(8)
    n4  = BTNode(4)
    n1  = BTNode(1)
    n5  = BTNode(5)
    n6  = BTNode(6)
    n7  = BTNode(7)
    n16 = BTNode(16)
    n14 = BTNode(14)
    n15 = BTNode(15)
    n12 = BTNode(12)
    n13 = BTNode(13)

    n11.left = n8
    n8.left = n4
    n4.left = n1
    n4.right = n5
    n5.right = n6
    n6.right = n7
    n11.right = n16
    n16.left = n14
    n14.left = n12
    n14.right = n15
    n12.right = n13

    res = inorderBSTSuccessor(n11, n7)
    val = None if not res else res.val
    print(val)
    print('----------')
    res = inorderBSTSuccessor(n11, n12)
    val = None if not res else res.val
    print(val)
    print('=============')

def test2():
    n11 = BTNode(11)
    n8  = BTNode(8)
    n4  = BTNode(4)
    n5  = BTNode(5)
    n6  = BTNode(6)
    n7  = BTNode(7)

    n11.left = n8
    n8.left = n4
    n4.right = n5
    n5.right = n6
    n6.right = n7

    res = inorderBSTSuccessor(n11, n11)
    val = None if not res else res.val
    print(val)
    print('----------')
    res = inorderBSTSuccessor(n11, n7)
    val = None if not res else res.val
    print(val)

if __name__ == '__main__':
    test1()
    test2()
