#!/usr/bin/python
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of
nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

leetcode #25
REDO: optionally, do it recursively. Learn how to reverse in one liner.
"""
from ListNode import ListNode

def revKGrp(root, k):
    """
    Performance 65% to 97%. 65ms fastest
    """
    if root is None or k < 2:
        return root

    t = None
    dm = ListNode(0)

    n_next = dm.next = b = root
    b_prev = dm
    count = 0
    while True:
        next_head = n_next
        for i in range(k - 1):
            next_head = next_head.next
            if not next_head:
                b_prev.next = n_next
                return dm.next

        while n_next and count < k:
            n = n_next
            n_next = n.next
            n.next = t
            t = n
            count += 1

        b_prev.next = t
        b_prev = b
        b = n_next

        if not n_next:
            return dm.next

        count = 0
        t = None

def reverseKGroup(self, head, k):
    """
    Taken from lc discussion. More elegantly written. I have not read through it carefully.
    """
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next

def revL(n):
    """
    Reverse a list in the normal way
    """
    t = None
    n_next = n

    while n_next:
        n = n_next
        n_next = n.next
        n.next = t
        t = n

    return t

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
    ListNode.print_ll(revKGrp(n1, 2))

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    ListNode.print_ll(revKGrp(n1, 3))

def test3():
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
    ListNode.print_ll(revKGrp(n1, 4))

if __name__ == '__main__':
    test1()
    test2()
    test3()
