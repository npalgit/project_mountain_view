#!/usr/bin/python
"""
Given a binary tree, return the preorder traversal of its nodes' values.
Bascially DFS.

#144
"""
from btNode import BTNode

def pot_stack(root):
    s = []
    rslt = []
    if not root: return rslt
    s.append(root)
    while s:
        n = s.pop()
        rslt.append(n.val)
        if n.right: s.append(n.right)
        if n.left: s.append(n.left)

    return rslt

def pot(n):
    """
    bascially dfs
    """
    rslt = []
    dfs(n, rslt)
    return rslt

def dfs(n, rslt):
    if not n: return
    rslt.append(n.val)
    dfs(n.left, rslt)
    dfs(n.right, rslt)

def test1():
    n1  = BTNode(1)
    n2  = BTNode(2)
    n3  = BTNode(3)
    n4  = BTNode(4)
    n5  = BTNode(5)
    n6  = BTNode(6)
    n7  = BTNode(7)
    n8  = BTNode(8)
    n9  = BTNode(9)
    n10 = BTNode(10)
    n11 = BTNode(11)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n4.left = n6
    n4.right = n7
    n3.left = n8
    n3.right = n9
    n8.left = n10
    n8.right = n11
    print(pot(n1))
    print(pot_stack(n1))

if __name__ == '__main__':
    test1()
