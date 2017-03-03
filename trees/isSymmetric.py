#!/usr/bin/python
from btNode import BTNode

def isSymmetric(root):
    return root == None or symHelper(root.left, root.right)

def symHelper(lhs, rhs):
    if lhs == None or rhs == None:
        return lhs == rhs
    if lhs.val != rhs.val:
        return False

    return symHelper(lhs.left, rhs.right) and symHelper(lhs.right, rhs.left)

def test1():
    n1 = BTNode(1)
    n2l = BTNode(2)
    n2r = BTNode(2)
    n3l = BTNode(3)
    n7l = BTNode(7)
    n7r = BTNode(7)
    n3r = BTNode(3)
    n4l = BTNode(4)
    n5l = BTNode(5)
    n6l = BTNode(6)
    n6r = BTNode(6)
    n5r = BTNode(5)
    n4r = BTNode(4)

    n1.left = n2l
    n1.right = n2r
    n2l.left = n3l
    n2l.right = n7l
    n2r.left = n7r
    n2r.right = n3r
    n3l.left = n4l
    n3l.right = n5l
    n7l.left = n6l
    n7r.right = n6r
    n3r.left = n5l
    n3r.right = n4r

    print(isSymmetric(n1))

def test2():
    n1 = BTNode(1)
    n2l = BTNode(2)
    n2r = BTNode(2)
    n3l = BTNode(3)
    n7l = BTNode(7)
    n7r = BTNode(7)
    n3r = BTNode(3)
    n4l = BTNode(4)
    n5l = BTNode(5)
    n6l = BTNode(6)
    n6r = BTNode(6)
    n5r = BTNode(5)
    n6 = BTNode(6)

    n1.left = n2l
    n1.right = n2r
    n2l.left = n3l
    n2l.right = n7l
    n2r.left = n7r
    n2r.right = n3r
    n3l.left = n4l
    n3l.right = n5l
    n7l.left = n6l
    n7r.right = n6r
    n3r.left = n5l
    n3r.right = n6

    print(isSymmetric(n1))

if __name__ == '__main__':
    test1()
    test2()
