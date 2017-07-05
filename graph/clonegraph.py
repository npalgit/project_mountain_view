#!/usr/bin/python
"""
Clone an undirected graph.
Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:
Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.
The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

#133
REDDO: Need to get this first try also do BFS.
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.dic = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self.dfs(node)

    def dfs(self, node):
        if not node: return None
        if node.label in self.dic:
            return self.dic[node.label]
        n_copy = UndirectedGraphNode(node.label)
        self.dic[node.label] = n_copy
        for n in node.neighbors:
            n_copy.neighbors.append(self.dfs(n))

        return n_copy

from collections import deque
class SolutionBFSTwoPass_r:
    """
    Acutally performs better than normal BFS, DFS. 91.84%
    """
    def __init__(self):
        self.dic = {}

    def cloneGraph(self, node):
        if not node: return
        self.copyNodes(node)
        self.copyEdges(node)
        return self.dic[node]

    def copyNodes(self, node):
        q = deque()
        q.append(node)
        self.dic[node] = UndirectedGraphNode(node.label)
        while q:
            n = q.popleft()
            for nbr in n.neighbors:
                if nbr not in self.dic:
                    self.dic[nbr] = UndirectedGraphNode(nbr.label)
                    q.append(nbr)

    def copyEdges(self, node):
        for old, copy in self.dic.iteritems():
            copy.neighbors = [self.dic[nbr] for nbr in old.neighbors]

class SolutionDFS_r:
    def __init__(self):
        self.dic = {}

    def cloneGraph(self, node):
        if not node: return

        return self.dfs(node)

    def dfs(self, node):
        if node in self.dic: return self.dic[node]

        copy_n = UndirectedGraphNode(node.label)
        self.dic[node] = copy_n
        for nbr in node.neighbors:
            copy_n.neighbors.append(self.dfs(nbr))

        return copy_n

class SolutionBFS_r:
    def __init__(self):
        self.dic = {}

    def cloneGraph(self, node):
        if not node: return
        q = deque()
        q.append(node)
        copy_n = UndirectedGraphNode(node.label)
        self.dic[node] = copy_n

        while q:
            n = q.popleft()
            copy_n = self.dic[n]

            for nbr in n.neighbors:
                if nbr not in self.dic.keys():
                    copy_nbr = UndirectedGraphNode(nbr.label)
                    self.dic[nbr] = copy_nbr
                    q.append(nbr)

                copy_n.neighbors.append(self.dic[nbr])

        return self.dic[node]


def test1():
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n3 = UndirectedGraphNode(3)
    n4 = UndirectedGraphNode(4)
    n5 = UndirectedGraphNode(5)
    n1.neighbors = [n2, n3, n5]
    n2.neighbors = [n1, n3, n4]
    n3.neighbors = [n1, n2, n5]
    n4.neighbors = [n2, n5]
    n5.neighbors = [n1, n5]

    sol = SolutionBFS_r()
    sol.cloneGraph(n1)
    for copy in sol.dic.values():
        print('n{}:{}'.format(copy.label, map(lambda x: x.label, copy.neighbors)))

if __name__ == '__main__':
    test1()
