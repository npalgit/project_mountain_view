#!/usr/bin/python
from heapq import *
"""
Given an array of integers arr where each element is at most k places
away from its sorted position, code an efficient function
sortKMessedArray that sorts arr. For instance, for an input array of
size 10 and k = 2, an element belonging to index 6 in the sorted array
will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
def sort(nums, k):
    """
    O(n) space
    """
    heap = nums[:k]
    heapify(heap)
    e = k
    res = []

    while e < len(nums):
        heappush(heap, nums[e])
        res.append(heappop(heap))
        e += 1

    while heap:
        res.append(heappop(heap))
        heapify(heap)

    return res

def sortLessSpace(nums, k):
    """
    O(1) space
    """
    heap = nums[:k]
    heapify(heap)
    e = k
    b = 0
    while e < len(nums):
        heappush(heap, nums[e])
        nums[b] = heappop(heap)
        b += 1
        e += 1

    while heap:
        nums[b] = heappop(heap)
        heapify(heap)
        b += 1

    return nums

def test1():
    nums = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    print(sort(nums, 2))
    print(sortLessSpace(nums, 2))

def test2():
    nums = [5, 1]
    print(sort(nums, 2))
    print(sortLessSpace(nums, 2))

if __name__ == '__main__':
    test1()
    test2()
