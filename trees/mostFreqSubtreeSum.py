#!/usr/bin/python
"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

leetcode#508
"""
from btNode import BTNode

max_f = 0 # note global variable on leetcode will result in the value being saved multiple times
def mfss(n):
    """
    92.8% performance first try
    """
    fd = {}
    mfss_helper(n, fd)
    print('{},{}'.format(max_f, fd))
    return [x for x in fd.keys() if fd[x] == max_f]

def mfss_helper(n, fd):
    if not n:
        return 0

    global max_f

    left = mfss_helper(n.left, fd)
    right = mfss_helper(n.right, fd)
    s = n.val + left + right
    freq = fd.get(s, 0) + 1
    fd[s] = freq
    if freq > max_f: max_f = freq
    return s

def test1():
    n5 = BTNode(5)
    n2 = BTNode(2)
    nm3 = BTNode(-3)

    n5.left = n2
    n5.right = nm3

    print(mfss(n5))

def test2():
    n5 = BTNode(5)
    n2 = BTNode(2)
    nm5 = BTNode(-5)

    n5.left = n2
    n5.right = nm5

    print(mfss(n5))

def test3():
    n1 = BTNode(1)

    print(mfss(n1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
