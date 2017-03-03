#!/usr/bin/python
from btNode import BTNode

def is_weight_balanced(n):
    if n is None:
        return (0, True)

    lhs = is_weight_balanced(n.left)

    if lhs[1] is False:
        return (0, False)

    rhs = is_weight_balanced(n.right)
    if rhs[1] is False:
        return (0, False)

    if lhs[0] != rhs[0]:
        return (0, False)

    return (lhs[0] + rhs[0] + n.val, True)


def test1():
    n4 =  BTNode(4)
    n1 = BTNode(1)
    n15 = BTNode(15)
    n3 = BTNode(3)
    n0 = BTNode(0)
    n2 = BTNode(2)
    n1a = BTNode(1)
    n1b = BTNode(1)
    n7 = BTNode(7)
    n15 = BTNode(15)

    n4.left = n1
    n4.right = n15
    n1.left = n3
    n1.right = n7
    n3.left = n0
    n3.right = n2
    n0.left = n1a
    n0.right = n1b
    n4.right = n15

    print(is_weight_balanced(n4))

def test2():
    n4 = BTNode(4)
    n1 = BTNode(1)
    n7 = BTNode(7)
    n3a = BTNode(3)
    n3b = BTNode(3)
    n0a = BTNode(0)
    n0b = BTNode(0)
    n0c = BTNode(0)
    n0d = BTNode(0)

    n4.left = n1
    n4.right = n7
    n1.left = n3a
    n1.right = n3b
    n3a.left = n0a
    n3a.right = n0b
    n0a.left = n0c
    n0c.left = n0d

    print(is_weight_balanced(n4))

def test3():
    n4 = BTNode(4)
    print(is_weight_balanced(n4))

def test4():
    n4 = BTNode(4)
    n3 = BTNode(2)
    n4.left = n3
    print(is_weight_balanced(n4))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
