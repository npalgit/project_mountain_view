#!/usr/bin/python
"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
#208
"""
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
    trie = Trie()
    trie.insert('hello')
    trie.insert('hell')
    print(trie.search('hell'))
    print(trie.search('hel'))
    print(trie.search('hello'))
    print(trie.startsWith('haaa'))
    print(trie.startsWith('hel'))

if __name__ == '__main__':
    test1()
