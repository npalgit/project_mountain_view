#!/usr/bin/python
"""
Implement LRU cache

#146
REDDO: review the trick, as it is a common interview question.
"""

class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LinkedNode(None, 'head') # head next is mru
        self.tail = LinkedNode(None, 'tail') # tail prev is lru
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def _deleteNode(self,node):
        assert(node is not self.head and node is not self.tail)
        del self.data[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def get(self,key):
        # using data.keys rather than just keys cause TLE in lc
        if key not in self.data.keys():
            return -1

        # sever node from the list
        node = self.data[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self._insertNew(node)

        return node.val

    def put(self, key, value):
        if key in self.data.keys():
            self._deleteNode(self.data[key])
        newNode = LinkedNode(key, value)
        self.data[key] = newNode
        self._insertNew(newNode)
        if len(self.data.keys()) > self.capacity:
            self._deleteNode(self.tail.prev)

    def _insertNew(self, newNode):
        newNode.next = self.head.next
        self.head.next.prev = newNode
        newNode.prev = self.head
        self.head.next = newNode

    def print_content(self):
        for k in self.data.keys():
            print(k, self.data[k].val)

        n = self.head
        l = []
        while n:
            l.append('({},{})'.format(n.key, n.val))
            n = n.next
        print('->'.join(l))
        print('------------')

def test1():
    cache = LRUCache(4)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    cache.print_content()
    cache.put('d', 4)
    cache.put('e', 5)
    cache.print_content()

    cache.get('c')
    cache.print_content()

    cache.put('b', 2)
    cache.print_content()

    cache.put('d', -1)
    cache.print_content()

if __name__ == '__main__':
    test1()
