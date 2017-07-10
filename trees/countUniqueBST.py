#!/usr/bin/python
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

#96
REDDO: figured out self with hints. must know
"""
def cntBST(n):
    if n == 1: return 1
    G = [1]*(n+1)
    for i_n in range(1,n+1):
        rslt = 0
        for i in range(i_n):
            rslt += G[i]*G[i_n-i-1]
        G[i_n] = rslt

    return G[-1]

# -------------- re-implement --------------------
def cntBST_r(n):
    ways = [0]*(n+1)
    ways[0] = 1
    for i_n in range(1, n+1):
        for idx in range(i_n):
            ways[i_n] += ways[idx]*ways[i_n-idx-1]

    return ways[-1]
# ------------------------------------------------

def test1():
    print(cntBST(3))
    print(cntBST_r(3))
    print(cntBST(4))
    print(cntBST_r(4))
    print(cntBST(5))
    print(cntBST_r(5))
    print(cntBST(6))
    print(cntBST_r(6))
    print(cntBST(0))
    print(cntBST_r(0))

if __name__ == '__main__':
    test1()
