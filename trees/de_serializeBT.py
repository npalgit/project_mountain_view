#!/usr/bin/python
"""
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

#297
REDO: Got this first try on my own. try to redo to practice different order traversal and iterative as tree exercises.
"""
class Codec:
    def __init__(self):
        self.s = ''
        self.i = 0

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return
        self.s += str(root.val)
        self.dfs_ser(root.left)
        self.dfs_ser(root.right)

        return self.s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        l = data.split(',')
        return self.dfs_des(l)

    def dfs_des(self, l):
        if self.i >= len(l) or l[self.i] == 'n':
            self.i += 1
            return None
        n = TreeNode(l[self.i])
        self.i += 1
        lhs = self.dfs_des(l)
        rhs = self.dfs_des(l)

        n.left = lhs
        n.right = rhs
        return n

    def dfs_ser(self, n):
        if not n:
            self.s += ',n'
            return

        self.s += ',{}'.format(n.val)

        self.dfs_ser(n.left)
        self.dfs_ser(n.right)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def print_nodes(n):
        if not n:
            return

        lhs = n.left.val if n.left else None
        rhs = n.right.val if n.right else None
        print('n={n_val}, {n_val}.left={lhs}, {n_val}.right={rhs}'.format(n_val=n.val, lhs=lhs, rhs=rhs))
        TreeNode.print_nodes(n.left)
        TreeNode.print_nodes(n.right)

def test1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n1.left = n2
    n2.left = n4
    n1.right = n3
    n3.left = n5
    n3.right = n6
    n6.left = n7
    n6.right = n8
    n8.right = n9

    codec = Codec()
    data = codec.serialize(n1)
    print(data)
    res = codec.deserialize(data)
    print(res)
    TreeNode.print_nodes(res)

if __name__ == '__main__':
    test1()
