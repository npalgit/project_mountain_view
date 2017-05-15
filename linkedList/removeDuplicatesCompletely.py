#!/usr/bin/python
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

#82
"""
from ListNode import ListNode

def removeDupComp(head):
    """
    Got this first try. 96.2% - 39.0% performance
    """
    if not head: return None
    dummy = ListNode(head.val-1)
    dummy.next = head
    i, j = dummy, dummy.next

    while j:
        if i.next == j:
            j = j.next
        elif i.next.val == j.val:
            while j and i.next.val == j.val:
                j = j.next
            i.next = j
        else:
            i = i.next
            j = j.next

    return dummy.next

def test1():
    n1  = ListNode(1)
    n2  = ListNode(2)
    n3a = ListNode(3)
    n3b = ListNode(3)
    n4a = ListNode(4)
    n4b = ListNode(4)
    n5  = ListNode(5)

    n1.next = n2
    n2.next = n3a
    n3a.next = n3b
    n3b.next = n4a
    n4a.next = n4b
    n4b.next = n5

    ListNode.print_ll(removeDupComp(n1))

def test2():
    n1  = ListNode(1)
    n1a = ListNode(1)
    n1b = ListNode(1)
    n2  = ListNode(2)
    n3  = ListNode(3)

    n1.next = n1a
    n1a.next = n1b
    n1b.next = n2
    n2.next = n3

    ListNode.print_ll(removeDupComp(n1))

def test3():
    n1  = ListNode(1)
    n1a = ListNode(1)
    n1b = ListNode(1)
    n2a  = ListNode(2)
    n2b  = ListNode(2)

    n1.next = n1a
    n1a.next = n1b
    n1b.next = n2a
    n2a.next = n2b

    ListNode.print_ll(removeDupComp(n1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
