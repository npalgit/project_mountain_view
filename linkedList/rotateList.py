#!/usr/bin/python
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

leetcode #61
REDO: clever solution
"""
from ListNode import ListNode

def rotateList(head, k):
    if head is None or head.next is None:
        return head

    leng = 1
    n = head

    # form a circle
    while n.next:
        n = n.next
        leng += 1

    n.next = head
    k = k % leng

    for i in xrange(leng - k):
        n = n.next

    rslt = n.next
    n.next = None

    return rslt

def rotateListLinear(head, k):
    if head is None or head.next is None:
        return head

    leng = 0
    n = head

    # go to the end find length
    while n:
        n = n.next
        leng += 1

    k = k % leng

    if k == 0:
        return head

    n = head
    for i in xrange(leng-k-1):
        n = n.next

    rslt = n.next
    t = n.next

    n.next = None
    while t.next:
        t = t.next
    t.next = head

    return rslt

def rotateListLinearDoesntWork(head, k):
    """
    Note: partially complete solution. Corner cases doesn't quite work.
    TODO: run the example and check for error output.
    """
    if head is None or head.next is None or k == 0:
        return head

    i = head.next
    idx = 0

    while i is not None and idx < k:
        idx += 1
        i = i.next

    if i is None:
        k = k % (idx + 1)
        i = head.next
        idx = 0
        while idx < k-1:
            idx += 1
            i = i.next

    j = head.next
    while i.next is not None:
        i = i.next
        j = j.next
    rslt = j.next
    j.next = None
    i.next = head

    return rslt

def generate_test_list1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    return n1

def generate_test_list2():
    n1 = ListNode(1)
    n2 = ListNode(2)

    n1.next = n2

    return n1

def generate_test_list3():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    return n1

def test1():
    print('----------------')
    head = generate_test_list1()
    rslt = rotateList(head, 0)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 0)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateList(head, 1)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateListLinear(head, 1)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateList(head, 2)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 2)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateList(head, 3)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 3)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateList(head, 4)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 4)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateList(head, 5)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateListLinear(head, 5)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateList(head, 6)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 6)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateList(head, 7)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 7)
    ListNode.print_ll(rslt)
    
    head = generate_test_list1()
    rslt = rotateList(head, 8)
    ListNode.print_ll(rslt)

    head = generate_test_list1()
    rslt = rotateListLinear(head, 8)
    ListNode.print_ll(rslt)

def test2():
    print('----------------')
    head = generate_test_list2()
    rslt = rotateList(head, 0)
    ListNode.print_ll(rslt)

    head = generate_test_list2()
    rslt = rotateListLinear(head, 0)
    ListNode.print_ll(rslt)

    head = generate_test_list2()
    rslt = rotateList(head, 1)
    ListNode.print_ll(rslt)

    head = generate_test_list2()
    rslt = rotateListLinear(head, 1)
    ListNode.print_ll(rslt)

    head = generate_test_list2()
    rslt = rotateList(head, 2)
    ListNode.print_ll(rslt)

    head = generate_test_list2()
    rslt = rotateListLinear(head, 2)
    ListNode.print_ll(rslt)

def test3():
    print('----------------')
    head = generate_test_list3()
    rslt = rotateList(head, 0)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 0)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateList(head, 1)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 1)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateList(head, 2)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 2)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateList(head, 3)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 3)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateList(head, 4)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 4)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateList(head, 5)
    ListNode.print_ll(rslt)

    head = generate_test_list3()
    rslt = rotateListLinear(head, 5)
    ListNode.print_ll(rslt)

if __name__ == '__main__':
    test1()
    test2()
    test3()
