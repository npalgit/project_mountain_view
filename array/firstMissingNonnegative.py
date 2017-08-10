#!/usr/bin/python
"""
Similar to firstMIssingPositive. except this one includes 0.
Given an array arr of unique nonnegative integers,
find the smallest nonnegative integer that is NOT in the array.
"""
def firstMissingNonnegative(nums):
    i = 0
    while i < len(nums):
        targ_idx = nums[i]
        if targ_idx != i and targ_idx < len(nums):
            nums[i], nums[targ_idx] = nums[targ_idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)

def test1():
    nums = [4, 0, 1, 2]
    print(firstMissingNonnegative(nums))

def test2():
    nums = [4, 3, 1, 2]
    print(firstMissingNonnegative(nums))

def test3():
    nums = [4, 3, 1, 2, 0]
    print(firstMissingNonnegative(nums))

def test4():
    nums = [4, 3, 2, 0, 5]
    print(firstMissingNonnegative(nums))

def test5():
    nums = []
    print(firstMissingNonnegative(nums))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
