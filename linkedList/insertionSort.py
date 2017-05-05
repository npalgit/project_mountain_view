#!/usr/bin/python
"""
Sort a linked list using insertion sort.
#147
Note: same solution TLE in python, but accepted in Java. See the Java solution for submission.
"""
from ListNode import ListNode
def insort(head):
    if not head: return None
    curr = head
    dummy_h = ListNode(0)

    while curr:
        hd = dummy_h
        while hd:
            if not hd.next or curr.val < hd.next.val:
                tail = hd.next
                hd.next = curr
                curr = curr.next
                hd.next.next = tail
                break

            hd = hd.next

    return dummy_h.next

def test1():
    l5 = ListNode(5)
    l3 = ListNode(3)
    l7 = ListNode(7)
    l9 = ListNode(9)
    l1 = ListNode(1)
    l0 = ListNode(0)
    l8 = ListNode(8)

    l5.next = l3
    l3.next = l7
    l7.next = l9
    l9.next = l1
    l1.next = l0
    l0.next = l8

    ListNode.print_ll(insort(l5))

if __name__ == '__main__':
    test1()
