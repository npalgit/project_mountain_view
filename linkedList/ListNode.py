class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def print_ll(n):
        l = []
        while n is not None:
           l.append(n.val)
           n = n.next
        print(l)
