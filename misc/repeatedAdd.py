#!/usr/bin/python
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
#258
"""
def add(n):
    if n/10 == 0:
        return n
    new_s = 0
    while n:
        new_s += n%10
        n /= 10

    return add(new_s)

def test1():
    print(add(3819))

if __name__ == '__main__':
    test1()
