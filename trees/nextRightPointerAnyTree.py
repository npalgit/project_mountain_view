#!/usr/bin/python
"""
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

#117
REDDO: tricky algo.
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
    curr = root
    head = None
    prev = None

    while curr:
        while curr:
            if curr.left:
                if prev:
                    prev.next = curr.left
                else:
                    head = curr.left
                prev = curr.left
            if curr.right:
                if prev:
                    prev.next = curr.right
                else:
                    head = curr.right
                prev = curr.right
            curr = curr.next

        curr = head
        head = None
        prev = None

    return root

def test1():
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n7 = TreeLinkNode(7)
    n8 = TreeLinkNode(8)
    n9 = TreeLinkNode(9)
    n10 = TreeLinkNode(10)
    n11 = TreeLinkNode(11)
    n12 = TreeLinkNode(12)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11
    n7.right = n12

    TreeLinkNode.print_nodes(connect(n1))
    print('--------------------')

def test2():
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.right = n5

    TreeLinkNode.print_nodes(connect(n1))

if __name__ == '__main__':
    test1()
    test2()
