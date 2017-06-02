#!/usr/bin/python
"""
Description see leetcode online
You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

#143
"""
from ListNode import ListNode

def reorderList(h):
    if not h or not h.next: return h
    lhs, rhs = splitList(h)
    h = merge(lhs, rhs)
    return h

def splitList(h):
    s = f = h
    while f.next and f.next.next:
        f = f.next.next
        s = s.next
    rhs = reverse(s.next)
    s.next = None

    return h, rhs

def merge(h, rhs):
    lhs = temp = h
    lhs = lhs.next
    while rhs:
        temp.next = rhs
        rhs = rhs.next
        temp = temp.next

        if lhs:
            temp.next = lhs
            lhs = lhs.next
            temp = temp.next

    return h

def reverse(n):
    tail = None

    while n:
        h = n
        n = n.next
        h.next = tail
        tail = h

    return tail

def test1():
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    ListNode.print_ll(reorderList(n0))

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    ListNode.print_ll(reorderList(n1))

def test3():
    n1 = ListNode(1)
    n2 = ListNode(2)

    n1.next = n2

    ListNode.print_ll(reorderList(n1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
