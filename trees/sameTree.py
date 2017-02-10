#!/usr/bin/python
from btNode import BTNode
"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

leetcode #100
"""
def isSameT(p, q):
    if p is None or q is None:
        return p == q

    if p.value != q.value:
        return False

    return isSameT(p.left, q.left) and isSameT(p.right, q.right)

def test1():
    n1a = BTNode(1)
    n1b = BTNode(1)

    n2a = BTNode(2)
    n2b = BTNode(2)

    n3a = BTNode(3)
    n3b = BTNode(3)

    n4a = BTNode(4)
    n4b = BTNode(4)

    n1a.left = n2a
    n2a.left = n3a
    n2a.right = n4a

    n1b.left = n2b
    n2b.left = n3b
    n2b.right = n4b

    print(isSameT(n1a, n1b))

def test2():
    n1a = BTNode(1)
    n1b = BTNode(1)

    n2a = BTNode(2)
    n2b = BTNode(2)

    n3a = BTNode(3)
    n3b = BTNode(3)

    n4a = BTNode(4)
    n4b = None

    n1a.left = n2a
    n2a.left = n3a
    n2a.right = n4a

    n1b.left = n2b
    n2b.left = n3b
    n2b.right = n4b

    print(isSameT(n1a, n1b))

def test3():
    print(isSameT(None, None))

def test4():
    n1a = BTNode(1)
    n1b = BTNode(1)

    n2a = BTNode(2)
    n2b = BTNode(2)

    n3a = BTNode(3)
    n3b = BTNode(3)

    n4a = BTNode(4)
    n5b = BTNode(5)

    n1a.left = n2a
    n2a.left = n3a
    n2a.right = n4a

    n1b.left = n2b
    n2b.left = n3b
    n2b.right = n5b

    print(isSameT(n1a, n1b))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
