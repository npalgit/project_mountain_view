#!/usr/bin/python
"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

#109
REDO: got O(nlogn) right away. review with O(n). Also notice pointer doesn't work in python
"""
from btNode import BTNode

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def count(head):
    k = 0
    while head:
        k += 1
        head = head.next
    return k

class LinkedListToTree:
    def __init__(self):
        self.node = None

    def ll2tfaster(self, head):
        self.node = head
        n = count(head)
        return self.ll2tfaster_dfs(n)

    def ll2tfaster_dfs(self, n):
        # n/2: left side length n/2
        # n-n/2-1: right_side_len: total_len - lft_len - mid
        # note: lhs = n/2-1, rhs = n-n/2 does not work
        # e.g. [1, 2, 3]
        if n == 0: return None
        lhs = self.ll2tfaster_dfs(n/2)
        tn = BTNode(self.node.val)
        self.node = self.node.next
        rhs = self.ll2tfaster_dfs(n -n/2-1)
        tn.left = lhs
        tn.right = rhs
        return tn

class LinkedListToTree2:
    def __init__(self):
        self.node = None

    def ll2tfaster2(self, head):
        self.node = head
        n = count(head)
        return self.ll2tfaster_dfs2(0, n-1)

    def ll2tfaster_dfs2(self, beg, end):
        if beg > end: return None

        mid = beg + (end-beg)/2

        lhs = self.ll2tfaster_dfs2(beg, mid-1)
        tn = BTNode(self.node.val)
        tn.left = lhs
        self.node = self.node.next
        rhs = self.ll2tfaster_dfs2(mid+1, end)
        tn.right = rhs
        return tn

def ll2t(head):
    """
    Accepted first try 66.6% peformance
    """
    if not head: return None
    if not head.next: return BTNode(head.val)

    fast = slow = head

    if fast.next and fast.next.next:
        fast = fast.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    n = BTNode(mid.val)
    slow.next = None
    n.left = ll2t(head)
    n.right = ll2t(mid.next)
    return n

def test1():
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
    l5.next = l6
    
    sol = LinkedListToTree()
    BTNode.print_nodes(sol.ll2tfaster(l1))
    print('-----------------')
    sol = LinkedListToTree2()
    BTNode.print_nodes(sol.ll2tfaster2(l1))
    print('-----------------')
    BTNode.print_nodes(ll2t(l1))
    print('====================')

def test2():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7

    sol = LinkedListToTree()
    BTNode.print_nodes(sol.ll2tfaster(l1))
    print('-----------------')
    sol = LinkedListToTree2()
    BTNode.print_nodes(sol.ll2tfaster2(l1))
    print('-----------------')
    BTNode.print_nodes(ll2t(l1))
    print('====================')

def test3():
    l1 = ListNode(1)

    sol = LinkedListToTree()
    BTNode.print_nodes(sol.ll2tfaster(l1))
    print('-----------------')
    sol = LinkedListToTree2()
    BTNode.print_nodes(sol.ll2tfaster2(l1))
    print('-----------------')
    BTNode.print_nodes(ll2t(l1))
    print('====================')

def test4():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2

    sol = LinkedListToTree()
    BTNode.print_nodes(sol.ll2tfaster(l1))
    print('-----------------')
    sol = LinkedListToTree2()
    BTNode.print_nodes(sol.ll2tfaster2(l1))
    print('-----------------')
    BTNode.print_nodes(ll2t(l1))
    print('====================')

def test5():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)

    l1.next = l2
    l2.next = l3

    sol = LinkedListToTree()
    BTNode.print_nodes(sol.ll2tfaster(l1))
    print('-----------------')
    sol = LinkedListToTree2()
    BTNode.print_nodes(sol.ll2tfaster2(l1))
    print('-----------------')
    BTNode.print_nodes(ll2t(l1))
    print('====================')

if __name__ == '__main__':
    test1()
    #test2()
    #test3()
    #test4()
    #test5()
