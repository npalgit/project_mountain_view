#!/usr/bin/python
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
#155
REDDO: figure out how to keep min for all stack
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stck = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curr_min = self.getMin()
        if curr_min == None or x < curr_min: # for some reason 'not curr_min' doesn't work
            curr_min = x
        self.stck.append((x, curr_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stck.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stck[-1][0] if self.stck else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stck[-1][1] if self.stck else None

def test1():
    pass

if __name__ == '__main__':
    test1()
