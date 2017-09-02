#!/usr/bin/python
"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
#325
"""

def maxSubarrayEqualsK(nums, k):
    max_len = 0
    curr_sum = 0
    # key: sum, val: idx
    dic = {0:-1}
    for idx, val in enumerate(nums):
        curr_sum += val
        targ = curr_sum-k

        if targ in dic:
            targ_idx = dic[targ]
            max_len = max(max_len, idx-targ_idx)

        if curr_sum not in dic:
            dic[curr_sum] = idx

    return max_len

def test1():
    nums = [1, -1, 5, -2, 3]
    print(maxSubarrayEqualsK(nums, 3))

if __name__ == '__main__':
    test1()
