#!/usr/bin/python
"""
remove duplicates from linkedlist
#83
"""
from ListNode import ListNode

def removeDup2(h):
    if not h:
        return None

    i = h
    j = h.next

    while j:
        while j and i.val == j.val:
            j = j.next

        i.next = j
        i = j

    return h

def removeDup(h):
    if not h:
        return None

    curr = h
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return h

def test1():
    n1a = ListNode(1)
    n1b = ListNode(1)
    n1c = ListNode(1)
    n2 = ListNode(2)
    n3a = ListNode(3)
    n3b = ListNode(3)
    n3c = ListNode(3)

    n1a.next = n1b
    n1b.next = n1c
    n1c.next = n2
    n2.next = n3a
    n3a.next = n3b
    n3b.next = n3c
    ListNode.print_ll(removeDup(n1a))

def test2():
    n1 = ListNode(1)
    ListNode.print_ll(removeDup(n1))

def test3():
    n1a = ListNode(1)
    n1b = ListNode(1)
    n1a.next = n1b
    ListNode.print_ll(removeDup(n1a))

if __name__ == "__main__":
    test1()
    test2()
    test3()
