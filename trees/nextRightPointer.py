#!/usr/bin/python
"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
#116
REDDO: quickly the iterative, sol with O(1) space.
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    @staticmethod
    def print_nodes(n):
        if not n:
            return

        lhs = n.left.val if n.left else None
        rhs = n.right.val if n.right else None
        nxt = n.next.val if n.next else None
        print('n={n_val}, {n_val}.left={lhs}, {n_val}.right={rhs}, {n_val}.next={nxt}'.format(n_val=n.val, lhs=lhs, rhs=rhs, nxt=nxt))
        TreeLinkNode.print_nodes(n.left)
        TreeLinkNode.print_nodes(n.right)

def connect(root):
    """
    Got recursion first try, but it is too slow. 0.62%!
    """
    if not root: return
    connectH(root.left, root.right)
    return root

def connectH(lhs, rhs):
    if not lhs or not rhs: return

    lhs.next = rhs
    connectH(lhs.left, lhs.right)
    connectH(lhs.right, rhs.left)
    connectH(rhs.left, rhs.right)

def connectIterative(root):
    """
    90.19% performance
    """
    lvl_start = root
    while lvl_start:
        curr = lvl_start
        while curr:
            if curr.left and curr.right: curr.left.next = curr.right
            if curr.right and curr.next: curr.right.next = curr.next.left

            curr = curr.next
        lvl_start = lvl_start.left
    return root

def test1():
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n6 = TreeLinkNode(6)
    n7 = TreeLinkNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    TreeLinkNode.print_nodes(n1)
    print('---------------')
    TreeLinkNode.print_nodes(connect(n1))
    print('---------------')

    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n6 = TreeLinkNode(6)
    n7 = TreeLinkNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    TreeLinkNode.print_nodes(connectIterative(n1))

if __name__ == '__main__':
    print('---------------')
    test1()
