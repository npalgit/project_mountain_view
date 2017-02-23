#!/usr/bin/python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
leetcode #33
REDO: maybe, got it first try. Do it both iteratively, smartly solution.
"""
def searchInSortedArraySmart(l, k):
    beg, end = 0, len(l)
    inf = 0x7fffffff
    n_inf = -inf-1

    while beg < end:
        mid = beg + (end-beg)/2
        if (l[0] > l[mid]) == (l[0] > k):
            num = l[mid]
        elif l[0] > k:
            num = n_inf
        else:
            num = inf

        if num == k:
            return mid
        if num < k:
            beg = mid+1
        else:
            end = mid

    return -1

def searchInSortedArrayIterative(l, k):
    beg, end = 0, len(l)-1
    # find division idx
    while beg < end:
       mid = beg + (end-beg)/2
       if l[mid] > l[end]:
           beg = mid+1
       else:
           end = mid

    # bin search
    rot = beg
    beg, end, n = 0, len(l)-1, len(l)
    while beg <= end:
        mid = beg+(end-beg)/2
        realmid = (mid + rot)%n

        if l[realmid] == k:
            return realmid
        if l[realmid] < k:
            beg = mid+1
        else:
            end = mid-1

    return -1

def searchInSortedArray(l, k):
    end = len(l)-1
    idx = find_idx(l, 0, end)

    if idx == -1:
        return bin_search(l, 0, end, k)

    lhs = bin_search(l, 0, idx, k)
    if lhs != -1:
        return lhs
    return bin_search(l, idx+1, end, k)

def find_idx(l, beg, end):
    if beg > end:
        return -1

    mid = beg + (end-beg)/2

    if mid+1 < len(l) and l[mid] > l[mid+1]:
        return mid

    if l[beg] > l[mid]:
        return find_idx(l, beg, mid)

    return find_idx(l, mid+1, end)

def bin_search(l, beg, end, k):
    if beg > end:
        return -1

    mid = beg + (end-beg)/2

    if l[mid] == k:
        return mid

    if l[mid] < k:
        return bin_search(l, mid+1, end, k)

    return bin_search(l, beg, mid-1, k)

def test1():
    l = [4, 5, 6, 7, 0, 1, 2]
    print(l)
    print(searchInSortedArraySmart(l, 5))
    print(searchInSortedArrayIterative(l, 5))
    print('--------------------')

def test2():
    l = [6, 7, 0, 1, 2, 3, 4]
    print(l)
    print(searchInSortedArraySmart(l, 2))
    print(searchInSortedArrayIterative(l, 2))
    print('--------------------')

def test3():
    l = [2, 3, 4, 6, 7, 8, 0, 1]
    print(l)
    print(searchInSortedArraySmart(l, 0))
    print(searchInSortedArrayIterative(l, 0))
    print('--------------------')

def test4():
    l = [1, 2, 3, 4, 5, 0]
    print(l)
    print(searchInSortedArraySmart(l, 0))
    print(searchInSortedArrayIterative(l, 0))
    print('--------------------')

def test5():
    l = [8, 0, 1, 2, 3, 4, 5]
    print(l)
    print(searchInSortedArraySmart(l, 2))
    print(searchInSortedArrayIterative(l, 2))
    print('--------------------')

def test6():
    l = [0, 1, 2, 3, 4, 5]
    print(l)
    print(searchInSortedArraySmart(l, 3))
    print(searchInSortedArrayIterative(l, 3))
    print('--------------------')

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

