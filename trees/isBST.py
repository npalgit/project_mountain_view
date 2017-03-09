#!/usr/bin/python
"""
check if a binary tree is BST
#98
"""
from btNode import BTNode

def isBST(n):
    int_max = 0x7fffffff
    int_min = -int_max-1
    return isB(n, int_max, int_min)

def isB(n, max_v, min_v):
    if not n:
        return True

    if n.val >= max_v or n.val <= min_v:
        return False

    return isB(n.left, n.val, min_v) and isB(n.right, max_v, n.val)

def test1():
    n1 = BTNode(1)
    print(isBST(n1))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)

    n1.left = n2
    print(isBST(n1))

def test3():
    n9 = BTNode(9)
    n5 = BTNode(5)
    n13 = BTNode(13)
    n3 = BTNode(3)
    n2 = BTNode(2)
    n4 = BTNode(4)
    n11 = BTNode(11)
    n21 = BTNode(21)

    n9.left = n5
    n9.right = n13
    n5.left = n3
    n3.left = n2
    n3.right = n4
    n13.left = n11
    n13.right = n21

    print(isBST(n9))

if __name__ == "__main__":
    test1()
    test2()
    test3()
