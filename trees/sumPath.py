#!/usr/bin/python
from btNode import BTNode

def pathSum(n, s, k):
    """
    Return whether a path from root to leaf path sumit to a target value, denoted by k.
    """
    if n is None:
        return False

    s += n.value
    if n.left is None and n.right is None and s == k:
        return True

    return pathSum(n.left, s, k) or pathSum(n.right, s, k)

def pathSumAlt(n, s):
    if n is None:
        return False
    s -= n.value
    if n.left is None and n.right is None and s == 0:
        return True

    return pathSumAlt(n.left, s) or pathSumAlt(n.right, s)

def test1():
    n5 =  BTNode(5)
    n4 =  BTNode(4)
    n8 =  BTNode(8)
    n11 = BTNode(11)
    n13 = BTNode(13)
    n4b = BTNode(4)
    n1 =  BTNode(1)
    n7 =  BTNode(7)
    n2 =  BTNode(2)

    n5.left = n4
    n4.left = n11
    n5.right = n8
    n8.left = n13
    n8.right = n4
    n4b.right = n1
    n4.left = n11
    n11.left = n7
    n11.right = n2

    print(pathSum(n5, 0, 22))
    print(pathSumAlt(n5, 22))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)

    n1.left = n2
    print(pathSum(n1, 0, 1))
    print(pathSumAlt(n1, 1))

if __name__ == '__main__':
    test1()
    test2()
