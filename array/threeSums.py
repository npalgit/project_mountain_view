#!/usr/bin/python
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

leetcode #15
REDDO defintily
"""

def threeSum(arr, targ):
    arr.sort()
    rslt = []

    # len(arr)-2 no need to look at last two element,
    # because you are looking for three sumes. won't have
    # enough elements for you
    for i in xrange(len(arr)-2):
        if i == 0 or (i >0 and arr[i] != arr[i-1]):
            rem = targ - arr[i]
            beg = i+1
            end = len(arr)-1
            # find two sums of the remaining.
            while beg < end:
                s = arr[beg] + arr[end]
                if s == rem:
                    rslt.append([arr[i], arr[beg], arr[end]])
                    while beg < end and (arr[beg] == arr[beg+1]):
                        beg += 1
                    while beg < end and (arr[end] == arr[end-1]):
                        end -= 1
                    beg += 1
                    end -= 1
                elif s < rem:
                    beg += 1
                else:
                    end -= 1
    return rslt

def threeSum_r(nums):
    nums.sort()
    res = []
    c = 0
    while c < len(nums)-2:
        imm_t = -nums[c]
        l = c + 1
        h = len(nums)-1
        while l < h:
            if nums[l] + nums[h] == imm_t:
                res.append([nums[c], nums[l], nums[h]])
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

    return res


def test1():
    arr = [-1, 0, 1, 2, -1, -4]
    print(threeSum(arr, 0))
    arr = [-1, 0, 1, 2, -1, -4]
    print(threeSum_r(arr))
    print('----------------')

def test2():
    arr = [-1, -1, -1, -1, -1]
    print(threeSum(arr, 0))
    arr = [-1, -1, -1, -1, -1]
    print(threeSum_r(arr))
    print('----------------')

def test3():
    arr = [-1, 0, 1, 2, 1, 2, -1, -1]
    print(threeSum(arr, 0))
    arr = [-1, 0, 1, 2, 1, 2, -1, -1]
    print(threeSum_r(arr))
    print('----------------')

def test4():
    arr = [1, -1, -1, 0]
    print(threeSum(arr, 0))
    arr = [1, -1, -1, 0]
    print(threeSum_r(arr))
    print('----------------')

def test5():
    arr = [-2, 0, 0, 2, 2]
    print(threeSum(arr, 0))
    arr = [-2, 0, 0, 2, 2]
    print(threeSum_r(arr))
    print('----------------')

def test6():
    arr = [-2, 0, 1, 1, 2]
    print(threeSum(arr, 0))
    arr = [-2, 0, 1, 1, 2]
    print(threeSum_r(arr))
    print('----------------')

def test7():
    arr = [3,0,-2,-1,1,2]
    print(threeSum(arr, 0))
    arr = [3,0,-2,-1,1,2]
    print(threeSum_r(arr))
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
