#!/usr/bin/python
"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

#99
#REDO: know how the algo works, no need to recode everything.
"""
from btNode import BTNode

class RT:
    def __init__(self):
        self.prev = BTNode(-0x7fffffff-1)
        self.first_n = None
        self.second_n = None

    def rt(self, n):
        self.traverse(n)
        self.first_n.val, self.second_n.val = self.second_n.val, self.first_n.val

    def traverse(self, n):
        if not n: return
        self.traverse(n.left)

        # understand the differences in those statements
        if self.prev.val > n.val:
            if not self.first_n:
                self.first_n = self.prev
            if self.first_n:
                self.second_n = n

        self.prev = n

        self.traverse(n.right)

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n6 = BTNode(6)

    n4.left = n6
    n6.left = n1
    n6.right = n3
    n4.right = n5
    n5.right = n2

    rt = RT()
    BTNode.print_nodes(n4)
    print('---------------')
    rt.rt(n4)
    BTNode.print_nodes(n4)

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)

    n2.right = n1

    rt = RT()
    BTNode.print_nodes(n2)
    print('---------------')
    rt.rt(n2)
    BTNode.print_nodes(n2)

if __name__ == '__main__':
    #test1()
    test2()
