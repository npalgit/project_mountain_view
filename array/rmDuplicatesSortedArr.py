#!/usr/bin/python
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
Note: my implementation print out the truncated array instead.
leetcode #26
"""
def rmDuplicatesSorted(l):
    if not l or len(l) == 1:
        return l

    i = 0
    for j in l:
        if l[i] != j:
            i += 1
            l[i] = j

    return l[:i+1]

def test1():
    l = [1, 2, 2, 3, 3, 3, 4]
    print(rmDuplicatesSorted(l))

def test2():
    l = [1, 1, 1, 1, 1, 2]
    print(rmDuplicatesSorted(l))

def test3():
    l = [1]
    print(rmDuplicatesSorted(l))

def test4():
    l = []
    print(rmDuplicatesSorted(l))
    
if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
