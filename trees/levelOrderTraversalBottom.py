#!/usr/bin/python
from btNode import BTNode

"""
]Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
leetcode #107
"""
def lotBottom(n):
    lst = []
    lot(n, 0, lst)

def lot(n, level, lst):
    if n is None:
        return

    if len(lst) < level + 1:
        lst.insert(0, [])

    lst[len(lst)-level-1].append(n.val)

    lot(n.left, level+1, lst)
    lot(n.right, level+1, lst)

def test1():
    n3 =  BTNode(3)
    n9 =  BTNode(9)
    n20 = BTNode(20)
    n15 = BTNode(15)
    n7 =  BTNode(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    lst = []
    lot(n3, 0, lst)
    print(lst)

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)
    n5 = BTNode(5)

    n1.left = n2
    n2.right = n3
    n3.right = n4
    n4.left = n5

    lst = []
    lot(n1, 0, lst)
    print(lst)

if __name__ == '__main__':
    test1()
    test2()
