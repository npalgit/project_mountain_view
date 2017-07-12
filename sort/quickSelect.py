#!/usr/bin/python
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.
#215
REDDO: great question
"""
def partition(nums, b, e, k):
    if b > e:
        return

    i = b-1
    pivot = nums[e]

    for j in range(b, e):
        if nums[j] >= pivot: # > or >= does not matter
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[e] = nums[e], nums[i+1]
    mid = i+1
    if mid == k: return nums[mid]
    if k < mid:
        return partition(nums, b, mid-1, k)
    else:
        return partition(nums, mid+1, e, k)

def test1():
    nums = [1, 8, 5, 2, 3, 6]
    # sorted: [1, 2, 3, 5, 6, 8]
    print(partition(nums, 0, len(nums)-1, 0))
    nums = [1, 8, 5, 2, 3, 6]
    print(partition(nums, 0, len(nums)-1, 1))
    nums = [1, 8, 5, 2, 3, 6]
    print(partition(nums, 0, len(nums)-1, 2))
    nums = [1, 8, 5, 2, 3, 6]
    print(partition(nums, 0, len(nums)-1, 3))
    nums = [1, 8, 5, 2, 3, 6]
    print(partition(nums, 0, len(nums)-1, 4))
    nums = [1, 8, 5, 2, 3, 6]
    print(partition(nums, 0, len(nums)-1, 5))

if __name__ == '__main__':
    test1()
