#!/usr/bin/python
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
#18
REDDO. even tho got this on the first try, after doing 3Sum, avoid duplicates annoying
"""

def fourS(nums, targ):
    """
    Maybe there is a more efficient way
    """
    n = len(nums)
    nums.sort()
    rslt = []
    for i in range(n-3):
        if i > 0 and nums[i-1] == nums[i]: continue

        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]: continue

            beg, end = j+1, n-1

            while beg < end:
                sums = nums[i] + nums[j] + nums[beg] + nums[end]
                if sums == targ:
                    rslt.append([nums[i], nums[j], nums[beg], nums[end]])
                    while beg < end and (nums[beg] == nums[beg+1]): beg += 1
                    while beg < end and (nums[end] == nums[end-1]): end -= 1
                    beg += 1
                    end -= 1
                elif sums < targ:
                    beg += 1
                else:
                    end -= 1
    return rslt

def fourSum_r(nums):
    nums.sort()
    i0 = 0
    res = []
    while i0 < len(nums)-3:
        threeSum_r(nums, i0, res)

        i0 += 1
        while i0 < len(nums)-3 and nums[i0-1] == nums[i0]:
            i0 += 1
    return res

def threeSum_r(nums, i0, res):
    c = i0+1
    while c < len(nums)-2:
        imm_t = -nums[i0]-nums[c]
        l = c + 1
        h = len(nums)-1
        while l < h:
            if nums[l] + nums[h] == imm_t:
                res.append([nums[i0], nums[c], nums[l], nums[h]])
                l += 1
                h -= 1
                while l < h and nums[l-1] == nums[l]:
                    l += 1
                while l < h and nums[h+1] == nums[h]:
                    h -= 1

            elif nums[l] + nums[h] < imm_t:
                l += 1
            else:
                h -= 1

        c += 1
        while c < len(nums) and nums[c-1] == nums[c]:
            c += 1

def test1():
   nums = [1, 0, -1, 0, -2, 2]
   print(fourS(nums, 0))
   nums = [1, 0, -1, 0, -2, 2]
   print(fourSum_r(nums))
   print('----------------')

def test2():
    nums = [-3,-2,-1,0,0,0,1,2,3]
    print(fourS(nums, 0))
    nums = [-3,-2,-1,0,0,0,1,2,3]
    print(fourSum_r(nums))
    print('----------------')

def test3():
    nums = [-1,2,2,-5,0,-1,4]
    print(fourS(nums, 0))
    nums = [-1,2,2,-5,0,-1,4]
    print(fourSum_r(nums))
    print('----------------')
    # rslt: [[-5,2,2,4],[-1,0,2,2]]

if __name__ == '__main__':
    test1()
    test2()
    test3()
