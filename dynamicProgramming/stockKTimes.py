#!/usr/bin/python
"""
Buy and sell stock with max k transactions
#188
REDO: excellent, watch out for corner cases. and begining index
"""
def bsStcksK(nums, k):
    n = len(nums)
    if k >= n/2:
        return bAll(nums)

    dp = [x[:] for x in [[0]*n]*(k+1)]
    for i in range(1, k+1):
        localMax = -nums[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], nums[j]+localMax)
            # or dp[i-1][j]-nums[j]
            localMax = max(localMax, dp[i-1][j-1]-nums[j])

    return dp[k][-1]

def bAll(nums):
    max_prof = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            max_prof += nums[i] - nums[i-1]
    return max_prof

def test1():
    nums = [1, 5, 0, 6, 5, 12, 9, 12, 7, 11]
    print(bsStcksK(nums, 3))

if __name__ == '__main__':
    test1()
