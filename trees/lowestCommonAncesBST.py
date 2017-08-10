#!/usr/bin/python
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#235
"""
from btNode import BTNode
def lcaBST(n, p, q):
    if not n or not p or not q: return None

    min_val = min(p.val, q.val)
    max_val = max(p.val, q.val)
    if min_val <= n.val and n.val <= max_val:
        return n

    if min_val >= n.val:
        return lcaBST(n.right, p, q)

    return lcaBST(n.left, p, q)

def test1():
    n15 = BTNode(15)
    n7  = BTNode(7)
    n30 = BTNode(30)
    n11 = BTNode(11)
    n9  = BTNode(9)
    n8  = BTNode(8)
    n10 = BTNode(10)
    n14 = BTNode(14)
    n13 = BTNode(13)
    n12 = BTNode(12)

    n15.left = n7
    n15.right = n30
    n7.right = n11
    n11.left = n9
    n11.right = n14
    n9.left = n8
    n9.right = n10
    n11.right = n14
    n14.left = n13
    n13.left = n12
    print(lcaBST(n15, n8, n12).val)
    print(lcaBST(n15, n13, n12).val)
    print(lcaBST(n15, n7, n12).val)

if __name__ == '__main__':
    test1()
