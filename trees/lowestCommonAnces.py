#!/usr/bin/python
"""
The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).
Find the lowest common ancestor.
#236
REDDO: figure out the algo quick
"""
from btNode import BTNode

def lca(n, p, q):
    if n == None or n == p or n == q: return n

    lhs = lca(n.left, p, q)
    rhs = lca(n.right, p, q)

    if lhs and rhs: return n
    return lhs if lhs else rhs

def lca_non_valid_node(node, t1, t2):
    both_true = [False]*2
    res = lca_nvn(node, t1, t2, both_true)
    if both_true[0] and both_true[1]:
        return res.val
    else:
        return -1

def lca_nvn(node, t1, t2, both_true):
    if not node:
        return None

    ret_n = None
    if node == t1 or node == t2:
        if node == t1:
            both_true[0] = True
        else:
            both_true[1] = True
        ret_n = node

    lhs = lca_nvn(node.left, t1, t2, both_true)
    rhs = lca_nvn(node.right, t1, t2, both_true)

    if lhs and rhs:
        return node

    if not ret_n:
        ret_n = lhs if lhs else rhs
    return ret_n

def test1():
    n3 = BTNode(3)
    n5 = BTNode(5)
    n6 = BTNode(6)
    n2 = BTNode(2)
    n7 = BTNode(7)
    n4 = BTNode(4)
    n1 = BTNode(1)
    n0 = BTNode(0)
    n8 = BTNode(8)

    n3.left = n5
    n5.left = n6
    n3.right = n1
    n5.right = n2
    n2.left = n7
    n2.right = n4
    n1.left = n0
    n1.right = n8

    n_nonvalid = BTNode(13)
    print(lca(n3, n6, n2).val)
    print(lca_non_valid_node(n3, n6, n_nonvalid))
    print(lca_non_valid_node(n3, n6, n2))
    print(lca_non_valid_node(n3, n4, n2))

if __name__ == '__main__':
    test1()
