#!/usr/bin/python

def quickSort(nums, b, e):
    if b > e: return
    p = partition(nums, b, e)
    quickSort(nums, b, p-1)
    quickSort(nums, p+1, e)

def partition(nums, b, e):
    i = b-1
    pivot = nums[e]

    for j in range(b, e):
        # < or <= does not matter as much
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[e] = nums[e], nums[i+1]
    print(nums)
    return i+1

def test1():
    nums = [1, 2, 3, 1, 2, 3, 4, 4, 5, 5, 6, 7, 6]
    quickSort(nums, 0, len(nums)-1)
    print(nums)

if __name__ == '__main__':
    test1()
