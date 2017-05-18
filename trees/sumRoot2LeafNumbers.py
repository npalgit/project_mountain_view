#!/usr/bin/python
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
#129
REDO: Do this fast, review. Got this after seeing the interesting algorithm
"""
from btNode import BTNode

def sumRoot2LeafNumbers(n):
    return sumHelper(n, 0)

def sumHelper(n, s):
    if not n: return 0
    if not n.left and not n.right:
        return s*10 + n.val

    return sumHelper(n.left, s*10+n.val) + sumHelper(n.right, s*10+n.val)

def test1():
    """
    No idea why this case doesn't quite work
    """
    n5 = BTNode(5)
    n4 = BTNode(4)
    n9 = BTNode(9)
    n7 = BTNode(7)
    n2 = BTNode(2)
    n8 = BTNode(8)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n1 = BTNode(1)

    n5.left = n4
    n5.right = n8
    n4.left = n9
    n9.left = n7
    n9.right = n2
    n8.left = n3
    n8.right = n4
    n4.right = n1

    print(sumRoot2LeafNumbers(n5))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n6 = BTNode(6)
    n7 = BTNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print(sumRoot2LeafNumbers(n1))

def test3():
    n5 = BTNode(5)
    n4 = BTNode(4)
    n9 = BTNode(9)
    n7 = BTNode(7)
    n2 = BTNode(2)

    n5.left = n4
    n4.left = n9
    n9.left = n7
    n5.right = n2
    print(sumRoot2LeafNumbers(n5))

if __name__ == '__main__':
    test1()
    test2()
    test3()
