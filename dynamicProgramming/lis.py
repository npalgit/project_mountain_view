#!/usr/bin/python
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
#300
#REDDO: binary search algorithm
"""
def lis(nums):
    dp = [0]*len(nums)
    for i in reversed(range(len(nums))):
        max_v = 0
        for j in reversed(range(i+1, len(nums))):
            if nums[i] < nums[j]:
                max_v = max(max_v, dp[j])

        dp[i] = max_v+1
        # equivalent one liner below
        # dp[i] = max([0] + [dp[j] for j in reversed(range(i+1, len(nums))) if nums[i] < nums[j]])+1
    return max(dp)

def lis_binsearch(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    max_len = 1
    for x in nums[1:]:
        if x > dp[max_len-1]:
            dp[max_len] = x
            max_len += 1
        else:
            idx = binSearch(dp, 0, max_len, x)
            dp[idx] = x

    return max_len


def binSearch(nums, b, e, k):
    while b < e:
        mid = b+(e-b)/2
        if k <= nums[mid]:
            e = mid
        else:
            b = mid+1
    return b

def test1():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis(nums))
    print(lis_binsearch(nums))

def test2():
    nums = [2, 2]
    print(lis(nums))
    print(lis_binsearch(nums))

def test3():
    nums = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10, 4, 5, 6, 7, 8]
    print(lis(nums))
    print(lis_binsearch(nums))

if __name__ == '__main__':
    test1()
    test2()
    test3()
