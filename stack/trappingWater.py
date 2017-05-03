#!/usr/bin/python
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#42
REDO: really proud, solved this myself. But redo for review
"""

def trappingW(nums):
    s = []
    n = len(nums)
    max_ar = i = 0
    while i < n:
        if not s or nums[i] <= nums[s[-1]]:
            s.append(i)
            i += 1
            continue

        bot = nums[s.pop()]
        if not s: continue

        il = s[-1]
        width = i - il-1
        ar = width*(min(nums[il], nums[i])-bot)
        max_ar += ar

    return max_ar

def test1():
    nums = [6, 3, 1, 2, 5, 7]
    print(trappingW(nums))

def test2():
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trappingW(nums))

if __name__ == '__main__':
    test1()
    test2()
