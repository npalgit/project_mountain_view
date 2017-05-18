#!/usr/bin/python
"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
#95
REDO: must know
"""
from btNode import BTNode

def buildUniqueBST(n):
    return trees(1, n)

def node(n, left, right):
    t = BTNode(n)
    t.left = left
    t.right = right

    return t

def trees(first, last):
    rslt = []
    for n in range(first, last+1):
        for left in trees(first, n-1):
            for right in trees(n+1, last):
                rslt.append(node(n, left, right))

    return rslt or [None]

def buildBST_dp(n):
    m_temp = [[[None]]*(n+2)]*(n+2)
    rslt = [x[:] for x in m_temp]

    ws = 0
    while ws < n:
        for i in xrange(1, n+1):
            j = i+ws
            if j > n:
                break

            rslt[i][j] = []
            m_l = rslt[i][j]

            for num in xrange(i, j+1):
                for l in rslt[i][num-1]:
                    for r in rslt[num+1][j]:
                        m_l.append(node(num, l, r))
        ws += 1
 
    return rslt[1][n]

def test1():
    rslt = buildUniqueBST(3)
    for t in rslt:
        BTNode.print_nodes(t)
        print('--------------')
    print('==============')
    rslt = buildBST_dp(3)
    for t in rslt:
        BTNode.print_nodes(t)
        print('--------------')
    print('==============')

def test2():
    #rslt = buildUniqueBST(4)
    rslt = buildBST_dp(4)
    for t in rslt:
        BTNode.print_nodes(t)
        print('--------------')
    print('==============')

def test3():
    #rslt = buildUniqueBST(0)
    rslt = buildBST_dp(0)
    print(rslt)
    print('==============')

if __name__ == '__main__':
    #test1()
    #test2()
    test3()
