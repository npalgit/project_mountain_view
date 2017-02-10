#!/usr/bin/python
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

      After removing the second node from the end, the linked list becomes 1->2->3->5.
      Note:
          Given n will always be valid.
          Try to do this in one pass.
leetcode #19
"""
from ListNode import ListNode

def removeNtoLast(ll, n):
    """
    This solution assumes that n can be larger than len(ll)
    """
    j = ll

    for idx in xrange(n):
        j = j.next

        if j is None and idx != n-1:
            return ll

    if j is None:
        return ll.next
    j = j.next
    i_b = ll

    while j is not None:
        j = j.next
        i_b = i_b.next

    # remove node
    i_b.next = i_b.next.next

    return ll

def test1():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ListNode.print_ll(l1)
    ListNode.print_ll(removeNtoLast(l1, 5))

def test2():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ListNode.print_ll(l1)
    ListNode.print_ll(removeNtoLast(l1, 4))

def test3():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ListNode.print_ll(l1)
    ListNode.print_ll(removeNtoLast(l1, 3))

def test4():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ListNode.print_ll(l1)
    ListNode.print_ll(removeNtoLast(l1, 2))

def test5():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    ListNode.print_ll(l1)
    ListNode.print_ll(removeNtoLast(l1, 1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
