#!/usr/bin/python
"""
Binary tree in order traversal.
#94
REDO iterative.
"""
from btNode import BTNode

def inOrderTrav(n, rslt):
    if not n:
        return

    inOrderTrav(n.left, rslt)
    rslt.append(n.val)
    inOrderTrav(n.right, rslt)

def inOrderTravRec(n):
    if not n:
        return None
    stck = []
    rslt = []

    while stck or n:
        if n:
            stck.append(n)
            n = n.left
        else:
            tmp = stck.pop()
            rslt.append(tmp.val)
            n = tmp.right

    return rslt

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n7 = BTNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.right = n7
    rslt = []
    inOrderTrav(n1, rslt)
    print(rslt)
    print(inOrderTravRec(n1))
    print("--------------")

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n7 = BTNode(7)

    n1.right = n2
    n2.right = n3
    n3.right = n4
    n4.right = n5
    n5.right = n7

    rslt = []
    inOrderTrav(n1, rslt)
    print(rslt)
    print(inOrderTravRec(n1))
    print("--------------")

def test3():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n7 = BTNode(7)

    n1.left = n2
    n2.left = n3
    n3.left = n4
    n4.left = n5
    n5.left = n7

    rslt = []
    inOrderTrav(n1, rslt)
    print(rslt)
    print(inOrderTravRec(n1))
    print("--------------")

if __name__ == "__main__":
    test1()
    test2()
    test3()
