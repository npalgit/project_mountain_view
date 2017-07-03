#!/usr/bin/python
"""
Given an array S of n integers, find three integers in S such that the
sum is closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#16
REDDO, and also all the sums. And various solutions.
"""
def threeSumClosest(nums, targ):
    nums.sort()
    n = len(nums)
    if n <= 3:
        return sum(nums)

    rslt = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        j = i+1
        k = n-1
        while j < k:
            sums = nums[i] + nums[j] + nums[k]
            if abs(targ-rslt) > abs(targ-sums):
                rslt = sums
                if rslt == targ:
                    return rslt

            if sums > targ:
                k -= 1
            else:
                j += 1
    return rslt

def test1():
   nums = [-1, 2, 1, -4]
   print(threeSumClosest(nums, 1))

def test2():
   nums = [1, 1, 1, 0]
   print(threeSumClosest(nums, -100))

def test3():
   nums = [1, -3, 3, 5, 4, 1]
   print(threeSumClosest(nums, 1))

if __name__ == '__main__':
    test1()
    test2()
    test3()
