#!/usr/bin/python
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
#445
"""
from ListNode import ListNode

def addTwoNums(l1, l2):
    if not l1 or not l2:
        return l1 if not l1 else l2

    stck_lhs, stck_rhs = [], []
    c_o = 0
    prepare_stck(stck_lhs, l1)
    prepare_stck(stck_rhs, l2)

    dummyN = ListNode(-1)
    while stck_lhs or stck_rhs or c_o:
        val_lhs = 0 if not stck_lhs else stck_lhs.pop().val
        val_rhs = 0 if not stck_rhs else stck_rhs.pop().val
        n_val = (c_o + val_lhs + val_rhs)%10
        c_o = (c_o + val_lhs + val_rhs)/10

        insert(dummyN, ListNode(n_val))

    return dummyN.next

def prepare_stck(stck, list_n):
    while list_n:
        stck.append(list_n)
        list_n = list_n.next

def insert(head, n):
    n.next = head.next
    head.next = n

def test1():
    n9 = ListNode(9)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1 = ListNode(1)
    n9.next = n4
    n4.next = n5
    n5.next = n1

    n8 = ListNode(8)
    n7 = ListNode(7)
    n2 = ListNode(2)
    n8.next = n7
    n7.next = n2

    res = addTwoNums(n9, n8)
    ListNode.print_ll(res)

if __name__ == '__main__':
    test1()
