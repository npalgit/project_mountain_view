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
REDDO: Got this first try on my own. try to redo to practice different order traversal and iterative as tree exercises.
"""
from collections import deque
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

    # --------------  redo pre-order ---------------------
    def serialize_r(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        n = root

        if not n: return ';'
        s = str(n.val)
        s = s + ',' + self.serialize_r(n.left)
        s = s + ',' + self.serialize_r(n.right)
        return s


    def deserialize_r(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_l = data.split(',')
        return self.dfs_deser_r(data_l)

    def dfs_deser_r(self, data_l):
        d = data_l[0]
        data_l.remove(d)
        if d == ';': return

        n = TreeNode(d)
        n.left = self.dfs_deser_r(data_l)
        n.right = self.dfs_deser_r(data_l)

        return n
    # -------------- end redo pre-order ---------------------

    # --------------  redo level-order ---------------------
    def serialize_level_r(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return
        q = deque()
        s = ''
        s += str(root.val)

        q.append(root)
        while q:
            n = q.popleft()
            s += ','

            if n.left:
                q.append(n.left)
                s += str(n.left.val)
            else:
                s += 'n'

            s += ','
            if n.right:
                q.append(n.right)
                s += str(n.right.val)
            else:
                s += 'n'
        return s

    def deserialize_level_r(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        data_l = data.split(',')
        d = data_l[0]
        data_l.remove(d)
        root = TreeNode(d)
        q = deque()
        q.append(root)

        while q:
            n = q.popleft()

            if data_l:
                left_d = data_l[0]
                data_l.remove(left_d)
                if left_d != 'n':
                    left = TreeNode(left_d)
                    n.left = left
                    q.append(left)

            if data_l:
                right_d = data_l[0]
                data_l.remove(right_d)
                if right_d != 'n':
                    right = TreeNode(right_d)
                    n.right = right
                    q.append(right)

        return root
    # -------------- end redo level-order ---------------------

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
    data = codec.serialize_level_r(n1)
    print(data)
    res = codec.deserialize_level_r(data)
    print(res)
    TreeNode.print_nodes(res)

if __name__ == '__main__':
    test1()
