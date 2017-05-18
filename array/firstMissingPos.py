#!/usr/bin/python
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

#41
REDO: need to figure out the trick first try. the corner cases on annoying.
"""
def firstmpos(nums):
    """
    my own solution
    """
    i = 0
    n = len(nums)
    while i < n:
        targ = nums[i]
        if targ-1 < n and targ-1 >= 0 and targ-1 != i and nums[targ-1] != nums[i]:
            nums[targ-1], nums[i] = nums[i], nums[targ-1]
        else:
            i += 1

    for i in range(n):
        if nums[i]-1 != i:
            return i+1
    return n+1

def firstmpos2(nums):
    """
    lc c++ solution. not better than mine
    """
    n = len(nums)
    for i in range(n):
        targ = nums[i]
        while targ-1 < n and targ-1 >= 0 and nums[targ-1] != nums[i]:
            nums[targ-1], nums[i] = nums[i], nums[targ-1]
            targ = nums[i]

    for i in range(n):
        if nums[i]-1 != i:
            return i+1
    return n+1

def test1():
   nums = [1, 2, 0]
   print(firstmpos(nums))
   nums = [1, 2, 0]
   print(firstmpos2(nums))
   print('-----------------')

def test2():
    nums = [3,4,-1,1]
    print(firstmpos(nums))
    nums = [3,4,-1,1]
    print(firstmpos2(nums))
    print('-----------------')

def test3():
    nums = []
    print(firstmpos(nums))
    nums = []
    print(firstmpos2(nums))
    print('-----------------')

def test4():
    nums = [0]
    print(firstmpos(nums))
    nums = [0]
    print(firstmpos2(nums))
    print('-----------------')

def test5():
    nums = [1]
    print(firstmpos(nums))
    nums = [1]
    print(firstmpos2(nums))
    print('-----------------')

def test6():
    nums = [1,1]
    print(firstmpos(nums))
    nums = [1,1]
    print(firstmpos2(nums))
    print('-----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
