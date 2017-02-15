#!/usr/bin/python
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
leetcode #24

Note: exactly the same as sample solution
"""
from ListNode import ListNode

def swapPairs(n):
    if not n or n.next is None:
        return n

    tmp = n.next
    n.next = swapPairs(n.next.next)
    tmp.next = n

    return tmp

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
    ListNode.print_ll(swapPairs(n1))
    print('--------------')

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    ListNode.print_ll(n1)
    ListNode.print_ll(swapPairs(n1))
    print('--------------')

def test3():
    n1 = ListNode(1)
    ListNode.print_ll(n1)
    ListNode.print_ll(swapPairs(n1))


if __name__ == '__main__':
    test1()
    test2()
    test3()
