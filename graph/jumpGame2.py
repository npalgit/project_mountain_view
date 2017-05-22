#!/usr/bin/python
"""
Given an array of non-negative integers, you are
initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#45
REDO: go over bfs solution.
"""
def jumpG(nums):
    """
    dynamic programming solution.
    91/92 test passed and time limit exceeded
    """
    if not nums or len(nums) == 1: return 0

    dp = [0]*len(nums)

    for i in range(len(nums)-2, -1, -1):
        min_jp = len(nums)
        for j_i in range(1, nums[i]+1):
            if i+j_i < len(nums):
                min_jp = min(min_jp, dp[i+j_i])
        dp[i] = min_jp + 1

    return dp[0]

def jumpGBFSSpaceEffic(nums):
    n_len, start, end = len(nums), 0, 0
    step = 0

    while end < n_len-1:
        maxend = end+1
        step += 1
        for i in range(start, end+1):
            if i+nums[i] >= n_len-1:
                return step
            maxend = max(maxend, i+nums[i])
        start, end = end+1, maxend
    return step

def test1():
    nums = [2, 3, 1, 1, 4]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test2():
    nums = [2,1]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test3():
    nums = [1, 1, 1, 2, 1, 1]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test4():
    nums = [2, 3, 0, 1, 4]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test5():
    nums = []
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test6():
    nums = [2]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

def test7():
    nums = [1, 2, 1, 1, 1]
    print(jumpG(nums))
    print(jumpGBFS(nums))
    print(jumpGBFSSpaceEffic(nums))
    print('--------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
