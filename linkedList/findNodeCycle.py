#!/usr/bin/python
"""
Given a linked list, find the node where the cycle begins if there is
a cycle in a linked list.

#142
REDO: being able to solve the math part on your own
"""
from ListNode import ListNode

def findCycleNode(h):
    slow = fast = h
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            slow1 = slow
            slow2 = h

            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next

            return slow

    return None

def test1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n8 = ListNode(8)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n6
    print(findCycleNode(n1).val)

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(findCycleNode(n1))

if __name__ == '__main__':
    test1()
    test2()
