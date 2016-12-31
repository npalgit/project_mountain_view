#!/usr/bin/python
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design
an algorithm that takes a list of n numbers as input and checks whether
there is a 132 pattern in the list.

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

-----------
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

-----------
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

def is132pattern(l):
    stck = []
    s3 = None
    for s1 in reversed(l):
        if s3 is not None and s1 < s3:
            return True

        while len(stck) != 0 and stck[-1] < s1:
            s3 = stck.pop()
        stck.append(s1)

    return False

def test1():
    l = [9, 11, 8, 9, 10, 7, 9]
    print(is132pattern(l))

def test2():
    l =[1, 2, 3, 4, 5]
    print(is132pattern(l))

def test3():
    l = [1, 1, 1, 1, 1, 1]
    print(is132pattern(l))

def test4():
    l = [1, 3, 2, 3, 4, 5, 12]
    print(is132pattern(l))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
