#!/usr/bin/python
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

leetcode #21

possibly REDDO. recursion is very smart. Try to do iteratively
"""
from ListNode import ListNode

def mergeList_r(n1, n2):
    dummy = ListNode(-1)
    curr_n = dummy

    while n1 and n2:
        if n1.val < n2.val:
            next_n = n1
            n1 = n1.next
        else:
            next_n = n2
            n2 = n2.next

        curr_n.next = next_n
        curr_n = curr_n.next

    curr_n.next = n1 if n1 else n2

    return dummy.next

def mergeLsRecur_r(n1, n2):
    if not n1 or not n2:
        return n1 if not n2 else n2

    if n1.val < n2.val:
        n1.next = mergeLsRecur_r(n1.next, n2)
        return n1

    n2.next = mergeLsRecur_r(n1, n2.next)
    return n2

def mtl_rec(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        l1.next = mtl_rec(l1.next, l2)
        return l1
    elif l2.val <= l1.val:
        l2.next = mtl_rec(l1, l2.next)
        return l2

def print_ll(n):
    l = []
    while n is not None:
       l.append(n.val)
       n = n.next
    print(l)

def test1():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l3
    l3.next = l5

    l2.next = l4
    l4.next = l6
    print_ll(l1)
    print_ll(l2)
    print_ll(mergeList_r(l1, l2))
    #print_ll(mtl_rec(l1, l2))

def test2():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3

    l4.next = l5
    l5.next = l6
    print_ll(l1)
    print_ll(l4)
    print_ll(mtl_rec(l1, l4))

def test3():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    print_ll(l1)
    print_ll(l6)
    print_ll(mtl_rec(l1, l6))

def test4():
    l1 = ListNode(1)
    l1b = ListNode(1)

    print_ll(l1)
    print_ll(l1b)
    print_ll(mtl_rec(l1, l1b))

if __name__ == '__main__':
    test1()
    #test2()
    #test3()
    #test4()
