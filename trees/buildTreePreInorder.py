#!/usr/bin/python
"""
Given inorder and preorder traversal of a tree, construct the binary tree.
#105
REDDO: can't find the trick right away. Very smart solution
"""
from btNode import BTNode

def buildT(pre_o, in_o):
    """
    60% percentile in leetcode
    """
    if in_o:
        mid = in_o.index(pre_o.pop(0))
        n = BTNode(in_o[mid])
        n.left = buildT(pre_o, in_o[:mid])
        n.right = buildT(pre_o, in_o[mid+1:])

        return n

def pre_process(in_o):
    dic = {}
    for i, item in enumerate(in_o):
        dic[item] = i

    return dic

def buildTHelper(pre_o, in_o, idx_dic, beg, end):
    if beg < end:
        mid = idx_dic[pre_o.pop(0)]
        n = BTNode(in_o[mid])
        n.left = buildTHelper(pre_o, in_o, idx_dic, beg, mid)
        n.right = buildTHelper(pre_o, in_o, idx_dic, mid+1, end)

        return n

def buildTFaster(pre_o, in_o):
    """
    95.3% percentile in leetcode.
    """
    idx_dic = pre_process(in_o)
    return buildTHelper(pre_o, in_o, idx_dic, 0, len(in_o))

def test1():
    n7 = BTNode(7)
    n10 = BTNode(10)
    n4 = BTNode(4)
    n3 = BTNode(3)
    n1 = BTNode(1)
    n2 = BTNode(2)
    n8 = BTNode(8)
    n11 = BTNode(11)

    n7.left = n10
    n7.right = n2
    n10.left = n4
    n10.right = n3
    n3.right = n1
    n2.left = n8
    n8.left = n11

    BTNode.print_nodes(n7)

    print('-----------------------------')
    pre_o = [7, 10, 4, 3, 1, 2, 8, 11]
    in_o = [4, 10, 3, 1, 7, 11, 8, 2]
    BTNode.print_nodes(buildT(pre_o, in_o))

    print('-----------------------------')
    pre_o = [7, 10, 4, 3, 1, 2, 8, 11]
    in_o = [4, 10, 3, 1, 7, 11, 8, 2]
    BTNode.print_nodes(buildTFaster(pre_o, in_o))

if __name__ == '__main__':
    test1()
