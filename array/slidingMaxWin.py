#!/usr/bin/python
"""
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

#239
REDO: good use of deque
"""
from collections import deque

def maxslidingWin(nums, k):
    q = deque()
    if not nums: return []
    rslt = [None]*(len(nums)-k+1)
    for i in range(len(nums)):
        if q and q[0] < i-k+1:
            q.popleft()
        while q and nums[i] > nums[q[-1]]:
            q.pop()

        q.append(i)

        if i >= k-1:
            rslt[i-k+1] = nums[q[0]]

    return rslt

def test1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxslidingWin(nums, k))

def test2():
     nums = [7,2,4]
     k = 2
     print(maxslidingWin(nums, 2))

if __name__ == '__main__':
    test1()
    test2()
