#!/usr/bin/python
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

#102
REDO: make sure can do this first try. should be fast
"""
from btNode import BTNode

def zzTrav(n):
    rslt = []
    dfs(n, 0, rslt)
    return rslt

def dfs(n, lvl, rslt):
    if not n: return

    if len(rslt)-1 < lvl: rslt.append([])
    if lvl%2 == 1:
        rslt[lvl].insert(0, n.val)
    else:
        rslt[lvl].append(n.val)

    dfs(n.left, lvl+1, rslt)
    dfs(n.right, lvl+1, rslt)

def test1():
    n3 = BTNode(3)
    n9 = BTNode(9)
    n20 = BTNode(20)
    n15 = BTNode(15)
    n7 = BTNode(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    print(zzTrav(n3))

if __name__ == '__main__':
    test1()
