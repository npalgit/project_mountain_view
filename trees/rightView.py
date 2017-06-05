#!/usr/bin/python
"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].
#199
#REDO: learn the trick quickly, cleaver algo
"""
from btNode import BTNode

def rightView(n):
    rslt = []
    traverse(n, 0, rslt)
    return rslt

def traverse(n, level, rslt):
    if not n: return

    if len(rslt) == level:
        rslt.append(n.val)

    traverse(n.right, level+1, rslt)
    traverse(n.left, level+1, rslt)

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n5 = BTNode(5)
    n7 = BTNode(7)
    n9 = BTNode(9)
    n8 = BTNode(8)

    n1.left = n2
    n2.left = n5
    n2.right = n9
    n5.left = n7
    n9.left = n8

    print(rightView(n1))

if __name__ == '__main__':
    test1()
