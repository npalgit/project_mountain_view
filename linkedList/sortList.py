#!/usr/bin/python
"""
Sort linkedlist
#148
"""
from ListNode import ListNode

def mergeSort(h):
    if not h or not h.next: return h
    s = f = h
    while f.next and f.next.next:
        f = f.next.next
        s = s.next

    rhs = mergeSort(s.next)
    s.next = None
    lhs = mergeSort(h)

    return merge(lhs, rhs)

def merge(lhs, rhs):
    dummyN = ListNode(-1)
    temp = dummyN
    while lhs and rhs:
        if lhs.val < rhs.val:
            temp.next = lhs
            lhs = lhs.next
        else:
            temp.next = rhs
            rhs = rhs.next
        temp = temp.next

    temp.next = lhs if not rhs else rhs
    return dummyN.next

def test1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n6.next = n5
    n5.next = n4
    n4.next = n3
    n3.next = n2
    n2.next = n1

    h = n6
    rslt = mergeSort(h)
    ListNode.print_ll(rslt)

def test2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n3.next = n2
    n2.next = n1

    h = n3
    rslt = mergeSort(h)
    ListNode.print_ll(rslt)

def test3():
    n1 = ListNode(1)
    n2 = ListNode(2)

    n2.next = n1

    h = n2
    rslt = mergeSort(h)
    ListNode.print_ll(rslt)

def test4():
    n1 = ListNode(1)

    h = n1
    rslt = mergeSort(h)
    ListNode.print_ll(rslt)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
