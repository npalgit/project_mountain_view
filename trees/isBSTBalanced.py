#!/usr/bin/python
"""
Given a BST, determine if it is height balanced.
#110
"""
from btNode import BTNode
def isBalBST(n):
    if isBal(n) == -1: return False
    return True

def isBal(n):
    if not n: return 0

    lhs = isBal(n.left)
    if lhs == -1: return -1

    rhs = isBal(n.right)
    if rhs == -1: return -1

    if abs(lhs-rhs) > 1: return -1

    return max(lhs, rhs) + 1

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n6 = BTNode(6)

    n3.left = n2
    n3.right = n5
    n2.left = n1
    n5.left = n4
    n5.right = n6

    print(isBalBST(n3))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)

    n1.left = n2
    n2.left = n3
    n3.left = n4
    print(isBalBST(n1))

if __name__ == '__main__':
    test1()
    test2()
