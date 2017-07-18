#!/usr/bin/python
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#42
REDDO: really proud, solved this myself. But redo for review
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
# ----------------------------------------------------
def trappingW_r(heights):
    stck = []
    stck.append(0)
    max_area = 0
    left_idx = 0
    curr = 1
    while curr < len(heights):
        if stck[-1] == left_idx and heights[curr] >= heights[left_idx]:
            left_idx = curr
            stck.pop()
            stck.append(curr)
            curr += 1
        elif heights[curr] < heights[stck[-1]]:
            stck.append(curr)
            curr += 1
        elif heights[curr] >= heights[stck[-1]]:
            base = heights[stck.pop()]
            h = min(heights[stck[-1]], heights[curr])
            w = curr-stck[-1]-1

            max_area += (h-base)*w

    return max_area
# ----------------------------------------------------
def trappingW_r2(heights):
    stck = []
    stck.append(0)
    max_area = 0
    for curr in range(1,len(heights)):
        while heights[curr] >= heights[stck[-1]]:
            base = heights[stck.pop()]
            if not stck: break
            h = min(heights[stck[-1]], heights[curr])
            w = curr-stck[-1]-1
            max_area += max(0, (h-base)*w)
        stck.append(curr)

    return max_area

def test1():
    nums = [6, 3, 1, 2, 5, 7]
    print(trappingW(nums))

def test2():
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trappingW(nums))

if __name__ == '__main__':
    test1()
    test2()
