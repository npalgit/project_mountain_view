#!/usr/bin/python
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
#212
"""
def ws(board, words):
    """
    Using a visited set. TLE with 36/37 passed
    """
    trie = Trie()
    board = [list(x) for x in board]
    for w in words: trie.insert(w)
    trieNode = trie.root
    trace = []
    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, i, j, trace, res, trieNode)
    return list(res)

def dfs(bd, i, j, trace, res, trieNode):
    if i < 0 or i >= len(bd) or j < 0 or j >= len(bd[0]) \
    or bd[i][j] == 'X' or not trieNode.containsKey(bd[i][j]): return
    trace.append(bd[i][j])
    if trieNode.get(bd[i][j]).isEnd:
        res.add(''.join(trace))

    trieNode = trieNode.get(bd[i][j])
    old_c = bd[i][j]
    bd[i][j] = 'X'

    dfs(bd, i+1, j, trace, res, trieNode)
    dfs(bd, i, j+1, trace, res, trieNode)
    dfs(bd, i, j-1, trace, res, trieNode)
    dfs(bd, i-1, j, trace, res, trieNode)
    trace.pop()
    bd[i][j] = old_c

def ws2(board, words):
    """
    Using a visited set. TLE with 36/37 passed
    """
    trie = Trie()
    visited = set()
    for w in words: trie.insert(w)
    trieNode = trie.root
    trace = []
    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs2(board, i, j, trace, res, visited, trieNode)
    return list(res)

def dfs2(bd, i, j, trace, res, visited, trieNode):
    if i < 0 or i >= len(bd) or j < 0 or j >= len(bd[0]) \
    or (i, j) in visited or not trieNode.containsKey(bd[i][j]): return
    trace.append(bd[i][j])
    visited.add((i, j))
    if trieNode.get(bd[i][j]).isEnd:
        res.add(''.join(trace))

    trieNode = trieNode.get(bd[i][j])
    dfs2(bd, i+1, j, trace, res, visited, trieNode)
    dfs2(bd, i-1, j, trace, res, visited, trieNode)
    dfs2(bd, i, j+1, trace, res, visited, trieNode)
    dfs2(bd, i, j-1, trace, res, visited, trieNode)
    trace.pop()
    visited.remove((i, j))

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = [None]*26

    def getIdx(self, ch):
        return ord(ch) - ord('a')

    def containsKey(self, ch):
        return self.links[self.getIdx(ch)] is not None

    def get(self, ch):
        return self.links[self.getIdx(ch)]

    def put(self, ch, node):
        self.links[self.getIdx(ch)] = node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)

        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)

        if node and node.isEnd:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)

        return node is not None

def test1():
    bds = [ \
        ['o','a','a','n'], \
        ['e','t','a','e'], \
        ['i','h','k','r'], \
        ['i','f','l','v']]

    words = ["oath","pea","eat","rain", 'eate', 'etae']
    print(ws(bds, words))

def test2():
    bds = ["aa"]
    words = ["aaaa"]
    print(ws(bds, words))

def test3():
    bds = ["aa"]
    words = ["a"]
    print(ws(bds, words))
if __name__ == '__main__':
    test1()
    test2()
    test3()
