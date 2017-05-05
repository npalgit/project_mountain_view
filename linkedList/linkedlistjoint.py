#!/usr/bin/python
"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

#160
REDO: the short code
"""
from ListNode import ListNode

def llintersectSimple(n1, n2):
    if not n1 or not n2: return None
    pA, pB = n1, n2

    while pA is not pB:
        pA = n2 if not pA else pA.next
        pB = n1 if not pB else pB.next

    return pA

def llintersect(n1, n2):
    """
    92.87% performance
    """
    pA, pB = n1, n2

    while pA and pB:
        pA = pA.next
        pB = pB.next

    if not pA:
        pA = n2
        while pB:
            pA = pA.next
            pB = pB.next
        pB = n1

    elif not pB:
        pB = n1
        while pA:
            pA = pA.next
            pB = pB.next
        pA = n2

    while pA is not pB:
        pA = pA.next
        pB = pB.next

    return pA

def test1():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l7 = ListNode(7)
    l9 = ListNode(9)
    l11 = ListNode(11)

    l1.next = l3
    l3.next = l5
    l5.next = l7
    l7.next = l9
    l9.next = l11
    l2.next = l4
    l4.next = l9
    print(llintersect(l1, l2).val)
    print(llintersectSimple(l1, l2).val)

def test2():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l7 = ListNode(7)
    l9 = ListNode(9)
    l11 = ListNode(11)

    l1.next = l3
    l3.next = l5
    l5.next = l7
    l7.next = l9
    l9.next = l11
    l2.next = l4
    l4.next = l5
    print(llintersect(l1, l2).val)
    print(llintersectSimple(l1, l2).val)

def test3():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l7 = ListNode(7)
    l9 = ListNode(9)
    l11 = ListNode(11)

    l1.next = l3
    l3.next = l5
    l5.next = l7
    l7.next = l9
    l9.next = l11
    l2.next = l4
    l4.next = l11
    print(llintersect(l1, l2).val)
    print(llintersectSimple(l1, l2).val)

if __name__ == '__main__':
    test1()
    test2()
    test3()
