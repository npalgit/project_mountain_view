#!/usr/bin/python
from ListNode import ListNode

def addTwoNumbers(n1, n2, co):
    if n1 is None and n2 is None:
        if co == 0:
            return None
        return ListNode(co)

    n1_val = 0
    n2_val = 0

    if n1 is not None:
        n1_val = n1.val
    if n2 is not None:
        n2_val = n2.val

    s = n1_val + n2_val + co
    new_n = ListNode(s%10)
    n1_next = None if n1 is None else n1.next
    n2_next = None if n2 is None else n2.next
    new_n.next = addTwoNumbers(n1_next, n2_next, s/10)

    return new_n

def addTwoNumbersNoCarry(n1, n2):
    if n1 is None and n2 is None:
        return None

    n1_val = 0 if n1 is None else n1.val
    n2_val = 0 if n2 is None else n2.val

    s = n1_val + n2_val

    new_n = ListNode(s%10)
    
    if s/10 == 1 and (n1 is None or n1.next is None):
        n1_next = ListNode(1)
    elif s/10 == 0 and (n1 is None or n1.next is None):
        n1_next = None
    else:
        n1.next.val = n1.next.val + s/10
        n1_next = n1.next

    n2_next = None if n2 is None else n2.next
    new_n.next = addTwoNumbersNoCarry(n1_next, n2_next)

    return new_n

def test1():
    n2 = ListNode(2)
    n4a = ListNode(4)
    n3 = ListNode(3)

    n5 = ListNode(5)
    n6 = ListNode(6)
    n4b = ListNode(4)
    
    n2.next = n4a
    n4a.next = n3

    n5.next = n6
    n6.next = n4b

    ListNode.print_ll(addTwoNumbers(n2, n5, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(n2, n5))

def test2():
    n2 = ListNode(2)
    
    ListNode.print_ll(addTwoNumbers(n2, None, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(n2, None))

def test3():
    n6 = ListNode(6)
    n7 = ListNode(7)
    n9 = ListNode(9)

    n5 = ListNode(5)

    n6.next = n7
    n7.next = n9
    ListNode.print_ll(addTwoNumbers(n6, n5, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(n6, n5))

def test4():
    n3 = ListNode(3)
    n4 = ListNode(4)
    n3.next = n4
    ListNode.print_ll(addTwoNumbers(None, n3, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(None, n3))

def test5():
    ListNode.print_ll(addTwoNumbers(None, None, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(None, None))

def test6():
    n6 = ListNode(6)
    n7 = ListNode(7)
    n9 = ListNode(9)

    n5 = ListNode(5)
    n8 = ListNode(8)
    n4 = ListNode(4)

    n6.next = n7
    n7.next = n9

    n5.next = n8
    n8.next = n4

    ListNode.print_ll(addTwoNumbers(n6, n5, 0))
    ListNode.print_ll(addTwoNumbersNoCarry(n6, n5))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
