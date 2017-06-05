#!/usr/bin/python
"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list
#138
REDO: interesting algorithm
"""

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    @staticmethod
    def print_ll(x):
        while x:
            if x.next:
                print('{}.next={}'.format(x.label, x.next.label))
            else:
                print('{}.next={}'.format(x.label, None))
            if x.random:
                print('{}.random={}'.format(x.label, x.random.label))
            else:
                print('{}.random={}'.format(x.label, None))
            x = x.next

def copyRandomPointer(head):
    if not head: return None
    dic = {}
    n = head
    while n:
        dic[n] = RandomListNode(n.label)
        n = n.next

    n = head

    for old, new in dic.iteritems():
        new.next = dic.get(old.next)
        new.random = dic.get(old.random)

    return dic.get(head)

def copyRandomPointerNoHash(head):
    if not head: return None
    n = head
    while n:
        np = RandomListNode(n.label)
        np.next = n.next
        n.next = np
        n = n.next.next

    # assign random pointer
    n = head
    while n:
        nrn = n.random.next if n.random else None
        n.next.random = nrn
        n = n.next.next

    n = head
    cloneHead = head.next
    nClone = cloneHead

    # for separating the two heads
    while nClone.next:
        n.next = nClone.next
        n = n.next
        nClone.next = n.next
        nClone = nClone.next
    n.next = None
    return cloneHead

def test1():
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n5 = RandomListNode(5)
    n8 = RandomListNode(8)
    n9 = RandomListNode(9)

    n1.next = n2
    n2.next = n3
    n3.next = n5
    n5.next = n8
    n8.next = n9
    n1.random = n5
    n2.random = n5
    n3.random = n5
    n8.random = n5
    n9.random = n5

    RandomListNode.print_ll(copyRandomPointer(n1))
    print('---------------')
    RandomListNode.print_ll(copyRandomPointerNoHash(n1))

if __name__ == '__main__':
    test1()
