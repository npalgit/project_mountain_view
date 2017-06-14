#!/usr/bin/python
"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Max Howell: Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so fuck off
#226
"""
from btNode import BTNode
def invertT(n):
    if not n: return
    n.left, n.right = invertT(n.right), invertT(n.left)
    return n

def test1():
    n4 = BTNode(4)
    n2 = BTNode(2)
    n1 = BTNode(1)
    n3 = BTNode(3)
    n7 = BTNode(7)
    n6 = BTNode(6)
    n9 = BTNode(9)

    n4.left = n2
    n4.right = n7
    n2.left = n1
    n2.right = n3
    n7.left = n6
    n7.right = n9

    invertT(n4)
    BTNode.print_nodes(n4)

if __name__ == '__main__':
    test1()
