#!/usr/bin/python
"""
LinkedIn hacker rank challenge.
In the actual hacker rank challenge, the pseudo-code was
given to you, you just had to implement it.

Build a BST, and insert each node, as the construction progresses.
Implment the insert function and at each level of insert,
print out the counter.
"""
class Counter:
    def __init__(self):
        self.val = 0

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def createBST(keys):
    counter = Counter()
    root = None

    for key in keys:
        if root:
            insert(root, key, counter)
        else:
            root = TreeNode(key)

        print(counter.val)

def insert(root, key, counter):
    counter.val += 1
    if key < root.val:
        if not root.left:
            root.left = TreeNode(key)
        else:
            insert(root.left, key, counter)
    else:
        if not root.right:
            root.right = TreeNode(key)
        else:
            insert(root.right, key, counter)

def test1():
    keys = [2, 1, 3]
    createBST(keys)
    print('------------')

def test2():
    keys = [1, 2, 3]
    createBST(keys)
    print('------------')

if __name__ == '__main__':
    test1()
    test2()
