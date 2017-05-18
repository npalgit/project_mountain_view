#!/usr/bin/python
"""
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

#75
REDO: many different algorithms. a few more than these. Do this without looking at sol. also dutch national flag. Four way partition?
"""
def sortColors(nums):
    """
    This essentially is the dutch national flag algorithm
    """
    l, h = 0, len(nums)-1
    while l <= h and nums[l] == 0: l += 1 # these are optional
    while h >= 0 and nums[h] == 2: h -= 1 # these are optional

    m = l
    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[h], nums[m] = nums[m], nums[h]
            h -= 1
        elif nums[m] == 1:
            m += 1

    return nums

def sortColors2(nums):
    """
    This essentially is the dutch national flag algorithm.
    """
    l, m, h = 0, 0, len(nums)-1

    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[h], nums[m] = nums[m], nums[h]
            h -= 1
        elif nums[m] == 1:
            m += 1

    return nums
def sortColors3(nums):
    i, j = 0, 0

    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
    return nums

def test1():
    nums = [0, 1, 2, 1, 1, 2, 1, 0, 0, 2]
    print(sortColors(nums))
    print(sortColors2(nums))
    print(sortColors3(nums))
    print('---------------')

def test2():
    nums = [2, 2, 2, 0, 0, 0, 0, 1, 1, 1]
    print(sortColors(nums))
    print(sortColors2(nums))
    print(sortColors3(nums))
    print('---------------')

def test3():
    nums = [0, 0]
    print(sortColors(nums))
    print('---------------')

def test4():
    nums = [2, 1]
    print(sortColors(nums))
    print('---------------')

def test5():
    nums = [2, 0, 0]
    print(sortColors(nums))
    print('---------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
