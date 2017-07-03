#!/usr/bin/python
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
leetcode #114
REDDO: smart solution
"""
from btNode import BTNode

def flatten(n):
    if not n:
        return

    left = n.left
    right = n.right

    flatten(left)
    flatten(right)

    n.left = None
    n.right = left

    curr = n
    while curr.right: curr = curr.right

    curr.right = right

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)
    n6 = BTNode(6)
    n7 = BTNode(7)
    n8 = BTNode(8)
    n9 = BTNode(9)

    n1.left = n2
    n2.left = n3
    n2.right = n4
    n4.left = n5
    n4.right = n6
    n1.right = n7
    n7.left = n8
    n7.right = n9

    flatten(n1)
    BTNode.print_nodes(n1)
    print('--------------------------')

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)

    n1.left = n2
    n2.left = n3

    flatten(n1)
    BTNode.print_nodes(n1)
    print('--------------------------')

def test3():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)

    n1.right = n2
    n2.right = n3

    flatten(n1)
    BTNode.print_nodes(n1)

if __name__ == '__main__':
    test1()
    test2()
    test3()
