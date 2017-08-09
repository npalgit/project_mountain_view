#!/usr/bin/python
"""
Twitter phone interview question.
Given N-ary node.
traverse it postorder way without using recurison.
each node has a pointer back to the top level parent.
and may has a pointer to left, which goes down to the next level.

An example is:
            1
           /
           2 -> 3 -> 4 -> 5
                /
              6 -> 7 -> 8
Post order traversal: [2, 6, 7, 8, 3, 4, 5, 1]
"""
class NAryNode:
    def __init__(self, val, left=None, parent=None, next=None):
        self.val = val
        self.left = left
        self.parent = parent
        self.next = next

def postOrderIterative(n):
    last = None
    while n:
        if last and last.parent == n:
            print(n.val)
            last = n
            n = n.next
            continue
        if n.left:
            last = n
            n = n.left
            continue

        print(n.val)
        last = n
        n = n.next

        if not n:
            n = last.parent

def test1():
    '''
            1
           /
           2 -> 3 -> 4 -> 5
                /
              6 -> 7 -> 8
    '''
    n1 = NAryNode(1)
    n2 = NAryNode(2)
    n3 = NAryNode(3)
    n4 = NAryNode(4)
    n5 = NAryNode(5)
    n6 = NAryNode(6)
    n7 = NAryNode(7)
    n8 = NAryNode(8)

    n1.left = n2
    n2.parent = n1
    n3.parent = n1
    n4.parent = n1
    n5.parent = n1
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n3.left = n6
    n6.parent = n3
    n7.parent = n3
    n8.parent = n3
    n6.next = n7
    n7.next = n8
    postOrderIterative(n1)
    print('---------------')

def test2():
    '''
            1
           /
           2 -> 3 -> 4 -> 5
          /
         6 -> 7 -> 8
    '''
    n1 = NAryNode(1)
    n2 = NAryNode(2)
    n3 = NAryNode(3)
    n4 = NAryNode(4)
    n5 = NAryNode(5)
    n6 = NAryNode(6)
    n7 = NAryNode(7)
    n8 = NAryNode(8)

    n1.left = n2
    n2.parent = n1
    n3.parent = n1
    n4.parent = n1
    n5.parent = n1
    n2.next = n3
    n3.next = n4
    n4.next = n5

    n2.left = n6
    n6.parent = n2
    n7.parent = n2
    n8.parent = n2
    n6.next = n7
    n7.next = n8
    postOrderIterative(n1)

if __name__ == '__main__':
    test1()
    test2()
