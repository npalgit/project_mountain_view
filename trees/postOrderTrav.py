#!/usr/bin/python
"""
Implement binary tree post order traversal

#145
REDO: as part of review for different traversal techniques. and iterative procedure as well
Note: got this first attempt
"""
from btNode import BTNode

def postOrderT(n):
    if not n: return []
    stck, l = [], []
    stck.append(n.val)
    postOrderDown(n, stck, l)
    return l

def postOrderDown(n, stck, l):
    if not n: return
    if n.right: stck.append(n.right.val)
    if n.left: stck.append(n.left.val)
    postOrderDown(n.left, stck, l)
    postOrderDown(n.right, stck, l)
    if stck and stck[-1] == n.val:
        l.append(stck.pop())

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n6 = BTNode(6)
    n7 = BTNode(7)
    n8 = BTNode(8)

    n1.left = n2
    n2.left = n3
    n2.right = n4
    n1.right = n6
    n6.left = n5
    n6.right = n8
    n8.left = n7
    print(postOrderT(n1))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)

    n1.right = n2
    n2.right = n3
    n3.right = n4

    print(postOrderT(n1))

if __name__ == '__main__':
    test1()
    test2()
