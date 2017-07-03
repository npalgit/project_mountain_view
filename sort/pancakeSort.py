#!/usr/bin/python
"""
pramp
"""

def pancakeSort(nums):
    for h in reversed(range(len(nums))):
        max_idx = findMaxIdx(nums, h)
        reverseK(nums, max_idx)
        reverseK(nums, h)

    return nums

def findMaxIdx(nums, h):
    max_v = nums[0]
    max_idx = 0
    for i in range(1, h+1):
        if nums[i] > max_v:
            max_v = nums[i]
            max_idx = i

    return max_idx

def reverseK(nums, k):
    i, j = 0, k
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def test1():
    nums = [7, 6, 4, 2, 6, 5, 1, 4, 3, 2]
    print(pancakeSort(nums))

def test2():
    nums = [7]
    print(pancakeSort(nums))

def test3():
    nums = []
    print(pancakeSort(nums))

if __name__ == '__main__':
    test1()
    test2()
    test3()
