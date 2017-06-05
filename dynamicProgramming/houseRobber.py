#!/usr/bin/python
"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.
#198
"""
def rob_dp(nums):
    n = len(nums)
    if n < 3: return max(nums)
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
    return max(dp[-1], dp[-2])

def rob(nums):
    n = len(nums)
    prevm0 = 0
    prevm1 = 0
    curr = 0
    for i in range(n):
        temp = max(prevm0, prevm1) + nums[i]
        prevm1 = prevm0
        prevm0 = curr
        curr = temp

    return max(prevm0, curr)

def robShort(nums):
        # based on the recursive formula below
        # f(0) = nums[0]
        # f(1) = max(num[0], num[1])
        # f(k) = max( f(k-2) + nums[k], f(k-1) )
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now

def test1():
    nums = [9, 1, 3, 5, 8, 11, 3]
    print(rob_dp(nums))
    print(rob(nums))
    print(robShort(nums))

if __name__ == '__main__':
    test1()
