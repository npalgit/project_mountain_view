#!/usr/bin/python
"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

leetcode #27
REDDO: do it fast in the most efficient solution. And fix removeElement2
review: both algorithms
"""
def removeElement(l, k):
    start, end = 0, len(l)-1

    while start <= end:
        if l[start] == k:
            tmp = l[start]
            l[start] = l[end]
            l[end] = tmp
            end -= 1
        else:
            start +=1

    return start

def removeElement3(l, k):
    n = len(l)
    i = 0
    for j in range(n):
        if l[j] != k:
            l[i], l[j] = l[j], l[i]
            i += 1

    return i

def test1():
    l = [3, 2, 2, 3]
    print(removeElement3(l, 3))
    l = [3, 2, 2, 3]
    print(removeElement(l, 3))

def test2():
    l = [3, 2, 2, 2, 3]
    print(removeElement3(l, 3))
    l = [3, 2, 2, 2, 3]
    print(removeElement(l, 3))

def test3():
    l = [3, 3]
    print(removeElement3(l, 3))
    l = [3, 3]
    print(removeElement(l, 3))

def test4():
    l = [4, 5]
    print(removeElement(l, 4))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
