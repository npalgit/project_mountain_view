#!/usr/bin/python
"""
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length

#80
REDO: same principle applies to remove 3 or 4
"""
def rmDupTwo(nums):
    i = 0

    for n in nums:
        if i < 2 or nums[i-2] < n:
            nums[i] = n
            i += 1
    print(nums)
    return i

def test1():
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6]
    print(rmDupTwo(nums))

if __name__ == '__main__':
    test1()
