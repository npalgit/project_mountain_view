#!/usr/bin/python
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
leetcode#23
"""
from ListNode import ListNode

def mergeKLL(lists):
    """
    Note: algorithm is the fastest but PriorityQue is not as fast as heapq
    """
    from Queue import PriorityQueue
    pq = PriorityQueue()

    rslt = ListNode(0)

    for node in lists:
        if node: pq.put((node.val, node))

    head = rslt
    while pq.qsize() > 0:
        node = pq.get()[1]
        head.next = node
        head = head.next

        if node.next:
            pq.put((node.next.val, node.next))

    return rslt.next

def test1():
    n1 = ListNode(1)
    n3 = ListNode(3)

    n2 = ListNode(2)
    n4 = ListNode(4)
    n14 = ListNode(14)
    n18 = ListNode(18)

    n7 = ListNode(7)
    n9 = ListNode(9)
    n11 = ListNode(11)
    n13 = ListNode(13)

    n1.next = n3
    l1 = n1

    n2.next = n4
    n4.next = n14
    n14.next = n18
    l2 = n2

    n7.next = n9
    n9.next = n11
    n11.next = n13
    l3 = n7

    lists = [l1, l2, l3]
    rslt = mergeKLL(lists)
    ListNode.print_ll(rslt)

if __name__ == '__main__':
    test1()






