#!/usr/bin/python
"""
Given a list of numbers, move 0's to the end while preserving its orders.
Actual facebook interview question
#283
"""

def moveZeroes(nums):
    i, j = 0, 0
    while j < len(nums):
        if nums[j] == 0:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1

    for idx in range(i, len(nums)):
        nums[idx] = 0

    return nums

def test1():
    nums = [5, 6, 7, 8, 1, 0]
    print(moveZeroes(nums))

def test2():
    nums = [0, 0, 0, 1, 3, 0, -1]
    print(moveZeroes(nums))

def test3():
    nums = [0, 0, 0, 0]
    print(moveZeroes(nums))

def test4():
    nums = [5, -1, 1, 2]
    print(moveZeroes(nums))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
