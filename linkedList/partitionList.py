#!/usr/bin/python
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
leetcode #86
"""
from ListNode import ListNode

def partitionList(n, x):
    h = ListNode(0)
    t = ListNode(0)
    h_n = h
    t_n = t

    while(n):
        if n.val < x:
            h_n.next = n
            h_n = h_n.next
        else:
            t_n.next = n
            t_n = t_n.next

        n = n.next

    h_n.next = t.next

    t_n.next = None
    return h.next

def test1():
    n1 = ListNode(1)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2a = ListNode(2)
    n5 = ListNode(5)
    n2b = ListNode(2)

    n1.next = n4
    n4.next = n3
    n3.next = n2a
    n2a.next = n5
    n5.next = n2b

    ListNode.print_ll(n1)
    ListNode.print_ll(partitionList(n1, 3))

if __name__ == "__main__":
    test1()
