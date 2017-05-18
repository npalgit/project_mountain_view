#!/usr/bin/python
"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

leetcode #27
REDO: do it fast in the most efficient solution. And fix removeElement2
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

def removeElement2(l, k):
    """
    make this one more efficent when time allows. Gave up does not work
    """
    if not l:
        return 0
    l_len = len(l)

    if l_len < 2:
        return 0 if l[0] == k else 1

    i, j = 0, 1 

    while j < len(l):
        if l[i] == k:
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp
            j += 1
        else:
            i += 1
    return i

def test1():
    l = [3, 2, 2, 3]
    print(removeElement2(l, 3))

def test2():
    l = [3, 2, 2, 2, 3]
    print(removeElement2(l, 3))

def test3():
    l = [3, 3]
    print(removeElement2(l, 3))

def test4():
    l = [4, 5]
    print(removeElement(l, 4))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
