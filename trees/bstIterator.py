#!/usr/bin/python
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

#173

REDO: must know
"""

from btNode import BTNode
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.s else False

    def next(self):
        """
        :rtype: int
        """
        n = self.s.pop()
        self.pushAll(n.right)
        return n.val

    def pushAll(self, n):
        while n:
            self.s.append(n)
            n = n.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
def test1():
    n7  = BTNode(7)
    n3  = BTNode(3)
    n1  = BTNode(1)
    n0  = BTNode(0)
    n2  = BTNode(2)
    n5  = BTNode(5)
    n4  = BTNode(4)
    n12 = BTNode(12)
    n10 = BTNode(10)
    n8  = BTNode(8)
    n9  = BTNode(9)
    n11 = BTNode(11)
    n15 = BTNode(15)

    n7.left = n3
    n3.left = n1
    n1.left = n0
    n1.right = n2
    n3.right = n5
    n5.left = n4
    n7.right = n12
    n12.left = n10
    n10.left = n8
    n8.right = n9
    n10.right = n11
    n12.right = n15

    i, v = BSTIterator(n7), []
    while i.hasNext(): v.append(i.next())
    print(v)

if __name__ == '__main__':
    test1()
