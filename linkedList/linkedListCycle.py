#!/usr/bin/python
"""
Detect if there is a cycle in the linked list
#141
"""
from ListNode import ListNode
def detectCycle(ll):
    if not ll or not ll.next: return False
    slow, fast = ll, ll.next
    while True:
        if slow == fast: return True
        if not fast or not fast.next: return False
        slow = slow.next
        fast = fast.next.next

def test1():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    l8 = ListNode(8)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = l8
    l8.next = l4

    print(detectCycle(l1))

if __name__ == '__main__':
    test1()
