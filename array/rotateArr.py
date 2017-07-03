#!/usr/bin/python
"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

#189
REDDO: the method with mod.
review: different methods
"""
def ra_mod(nums, k):
    """
    comment: draw out a circle of the array.
    you go around each k step. There are two possiblity.
    1. the circle will end where it starts.
    2. it does not end where it starts.
    Since it is a circle, it does not matter where we start.
    We will have only 1 or 2 above.

    situation 1. we start the circle again at the next index.
        since the first ended where it started. We know that start+1
        has not been touched. If it is touched that means we are taking
        step 1 each time, and consequently count would've been reached
        as well.
    situation 2. we know it will traverse all elements. because 
        first time it goes around it did not end up at start. but 
        ends up at some index past the first. We can see it as 
        the second cycle. Since its a circle starting point does not
        matter, we know that the second iteration, it will not end 
        where it begins either, the iteration ends when count gets
        reached.

    """
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
