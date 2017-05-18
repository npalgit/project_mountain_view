#!/usr/bin/python
"""
Given an array of n positive integers and a positive integer s,
 find the minimal length of a contiguous subarray of which the sum ≥ s.
 If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of
which the time complexity is O(n log n).
#209
REDO: optional, look up O(nlog(n)) solution.
"""

def minssa(s, nums):
    temp_s = 0
    left = 0
    win_s = len(nums)+1
    for right in range(len(nums)):
        temp_s += nums[right]

        while temp_s >= s:
            if right-left+1 < win_s:
                win_s = right-left+1
            temp_s -= nums[left]
            left += 1

    return 0 if win_s == len(nums)+1 else win_s

def test1():
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(minssa(7, nums))

if __name__ == '__main__':
    test1()
