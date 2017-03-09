#!/usr/bin/python
"""
Given inorder and postorder traversal of a tree, construct the binary tree.
similar to #105
#106
"""
from btNode import BTNode

def buildT(post_o, in_o):
    """
    68% percentile in leetcode
    """
    if in_o:
        mid = in_o.index(post_o.pop())
        n = BTNode(in_o[mid])
        n.right = buildT(post_o, in_o[mid+1:])
        n.left = buildT(post_o, in_o[:mid])

        return n

def pre_process(in_o):
    dic = {}
    for i, item in enumerate(in_o):
        dic[item] = i

    return dic

def buildTHelper(post_o, in_o, idx_dic, beg, end):
    if beg < end:
        mid = idx_dic[post_o.pop()]
        n = BTNode(in_o[mid])
        n.right = buildTHelper(post_o, in_o, idx_dic, mid+1, end)
        n.left = buildTHelper(post_o, in_o, idx_dic, beg, mid)

        return n

def buildTFaster(post_o, in_o):
    """
    95.3% percentile in leetcode.
    """
    idx_dic = pre_process(in_o)
    return buildTHelper(post_o, in_o, idx_dic, 0, len(in_o))

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
    post_o = [4, 1, 3, 10, 11, 8, 2, 7]
    in_o = [4, 10, 3, 1, 7, 11, 8, 2]
    BTNode.print_nodes(buildT(post_o, in_o))

    print('-----------------------------')
    post_o = [4, 1, 3, 10, 11, 8, 2, 7]
    in_o = [4, 10, 3, 1, 7, 11, 8, 2]
    BTNode.print_nodes(buildTFaster(post_o, in_o))
    print('-----------------------------')

def test2():
    post_o = [2, 1]
    in_o = [2, 1]
    BTNode.print_nodes(buildT(post_o, in_o))

    print('-----------------------------')
    post_o = [2, 1]
    in_o = [2, 1]
    BTNode.print_nodes(buildT(post_o, in_o))

if __name__ == '__main__':
    test1()
    test2()
