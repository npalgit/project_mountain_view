#!/usr/bin/python
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
leetcode #92
"""
from ListNode import ListNode

def rotateLSegment(l, m, n):
    dummyN = ListNode(0)
    dummyN.next = l

    l = dummyN
    rslt, i = l, 0

    while i < m-1:
        l = l.next
        i += 1

    t, i = None, 0

    beg, end = l, l.next
    l = l.next

    while l and i <= n-m:
        h = l
        l = l.next
        h.next = t
        t = h
        i += 1

    beg.next = t
    end.next = l

    return dummyN.next

def test1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    ListNode.print_ll(n1)
    ListNode.print_ll(rotateLSegment(n1, 2, 5))
    print('------------------')

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    ListNode.print_ll(n1)
    ListNode.print_ll(rotateLSegment(n1, 1, 4))

if __name__ == "__main__":
    test1()
    test2()
