#!/usr/bin/python
"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
#203
"""
from ListNode import ListNode

def removeElement(n, val):
    dummyN = ListNode(-1)
    dummyN.next = n
    h = dummyN
    while h:
        if h.next and h.next.val == val:
            h.next = h.next.next
        else:
            h = h.next

    return dummyN.next

def test1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n6a = ListNode(6)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6b = ListNode(6)

    n1.next = n2
    n2.next = n6a
    n6a.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6b

    rslt = removeElement(n1, 6)
    print(ListNode.print_ll(rslt))

def test2():
    n1a = ListNode(1)
    n1b = ListNode(1)
    n1c = ListNode(1)

    n1a.next = n1b
    n1b.next = n1c
    rslt = removeElement(n1a, 1)
    print(ListNode.print_ll(rslt))

if __name__ == '__main__':
    test1()
    test2()
