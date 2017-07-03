#!/usr/bin/python
"""
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length

#80
REDDO: same principle applies to remove 3 or 4
"""
def rmDupTwo(nums):
    """
    This solution does not get accepted either
    """
    i = 0

    for n in nums:
        if i < 2 or nums[i-2] < n:
            nums[i] = n
            i += 1
    print(nums)
    return i

def rmDupTwo_count_r(nums):
    """
    For somereason this solution does not get accepted in leetcode
    """
    if len(nums) <= 2: return len(nums)
    i = 1
    count = 0

    for j in range(1, len(nums)):
        if nums[j-1] == nums[j]:
            count += 1
        else:
            count = 0
        if count < 2:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return i

def test1():
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6]
    print(rmDupTwo(nums))
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6]
    print(rmDupTwo_count_r(nums))
    print('------------')

def test2():
    nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
    print(rmDupTwo(nums))
    nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
    print(rmDupTwo_count_r(nums))
    print('------------')

def test3():
    nums = [1, 1, 1]
    print(rmDupTwo(nums))
    nums = [1, 1, 1]
    print(rmDupTwo_count_r(nums))
    print('------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
