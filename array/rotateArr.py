#!/usr/bin/python
"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

#189
REDO: the method with mod.
"""
def ra_mod(nums, k):
    cnt, n = 0, len(nums)
    k %= n
    start = 0
    while cnt < n:
        # first swap
        tmp = nums[start]
        idx = start
        n_idx = (idx+k)%n
        n_tmp = nums[n_idx]
        nums[n_idx] = tmp
        idx = n_idx
        tmp = n_tmp
        cnt += 1
        while idx != start:
            n_idx = (idx+k)%n
            n_tmp = nums[n_idx]
            nums[n_idx] = tmp
            idx = n_idx
            tmp = n_tmp
            cnt += 1

        start += 1
    return nums

def ra_rev(nums, k):
    k %= len(nums)
    rev(nums, 0 , len(nums)-1)
    rev(nums, 0, k-1)
    rev(nums, k, len(nums)-1)

    return nums

def rev(nums, b, e):
    while b < e:
        nums[b], nums[e] = nums[e], nums[b]
        b += 1
        e -= 1

def test1():
    nums = [0, 1, 2, 3, 4, 5, 6]
    k = 3
    print(ra_mod(nums, k))
    nums = [0, 1, 2, 3, 4, 5, 6]
    print(ra_rev(nums, k))

def test2():
    nums = [5, 6, 7, 8, 9, 10]
    k = 2
    print(ra_mod(nums, k))
    nums = [5, 6, 7, 8, 9, 10]
    print(ra_rev(nums, k))

if __name__ == '__main__':
    test1()
    test2()
