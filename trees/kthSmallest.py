#!/usr/bin/python
"""
Given a BST, return the kth smallest 
#230
REDO: the other two methods. the current one is great.
"""
from btNode import BTNode
def dfs(n, counter, k):
    if not n: return
    lhs = dfs(n.left, counter, k)
    if lhs: return lhs

    counter[0] += 1
    if counter[0] == k:
        return n.val
    rhs = dfs(n.right, counter, k)
    if rhs: return rhs
    return 0

def test1():
    n1 = BTNode(1)
    n3 = BTNode(3)
    n5 = BTNode(5)
    n9 = BTNode(9)
    n7 = BTNode(7)
    n6 = BTNode(6)
    n8 = BTNode(8)
    n13 = BTNode(13)
    n11 = BTNode(11)

    n5.left = n3
    n3.left = n1
    n5.right = n9
    n9.left = n7
    n7.left = n6
    n7.right = n8
    n9.right = n13
    n13.left = n11

    res = dfs(n5, [0], 8)
    print(res)

if __name__ == '__main__':
    test1()
