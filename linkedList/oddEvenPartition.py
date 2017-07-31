#!/usr/bin/python
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on

#328
"""

from ListNode import ListNode

def oddEvenPartition(n):
    if not n or not n.next:
        return n
    odd = n
    even = n.next
    even_head = n.next

    while even and even.next:
        odd.next = even.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
        odd.next = even_head

    return n

def test1():
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

    res = oddEvenPartition(n1)
    ListNode.print_ll(res)

if __name__ == '__main__':
    test1()
