#!/usr/bin/python

def nextPerm(nums):
    i = len(nums)-1
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1
    i1 = i-1
    if i1 >= 0:
        j = len(nums)-1
        while j >= i1 and nums[j] <= nums[i1]:
            j -= 1
        nums[i1], nums[j] = nums[j], nums[i1]
    reverse(nums, i, len(nums)-1)

def nextPerm2(nums):
    i = len(nums)-2
    while i >= 0 and nums[i+1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = len(nums)-1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i+1, len(nums)-1)

def reverse(nums, beg, end):
    while beg <= end:
        nums[beg], nums[end] = nums[end], nums[beg]
        beg += 1
        end -=1

def test1():
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nextPerm(nums)
    print(nums)
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nextPerm2(nums)
    print(nums)

def test2():
    nums = [5, 4, 3, 2, 1]
    nextPerm(nums)
    print(nums)
    nums = [5, 4, 3, 2, 1]
    nextPerm2(nums)
    print(nums)

def test3():
    nums = [1, 1, 1, 1, 2]
    nextPerm(nums)
    print(nums)
    nums = [1, 1, 1, 1, 2]
    nextPerm2(nums)
    print(nums)

def test4():
    nums = [1, 5, 1]
    nextPerm(nums)
    print(nums)

if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    test4()

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
#31
REDO: smart algo
"""
