#!/usr/bin/python
"""
Find the maximum Depth of Binary Tree
#104
Note: no test case needed, very simple question
"""
def max_depth(n):
    return 1+max(max_depth(n.left), max_depth(n.right)) if n else 0

def test1():
    pass

if __name__ == '__main__':
    test1()
