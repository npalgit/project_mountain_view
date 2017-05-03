#!/usr/bin/python
"""
Find the min height of the tree. Note the special case from root to leaf.

#111
"""
def minH(n):
    if not n: return 0
    lhs = minH(n.left)
    rhs = minH(n.right)
    if lhs == 0 or rhs == 0:
        return lhs + rhs + 1

    return min(lhs, rhs) + 1

def test1():
    pass

if __name__ == '__main__':
    test1()
