#!/usr/bin/python

def sort(nums):
    divide(nums, 0, len(nums)-1)

def divide(nums, beg, end):
    if beg == end: return
    print(beg, end)
    mid = beg + (end - beg)/2
    divide(nums, beg, mid)
    divide(nums, mid+1, end)
    merge(nums, beg, mid, end)

def merge(nums, b, m, e):
    lhs, rhs = [], []
    for i in range(b, m+1): lhs.append(nums[i])
    for j in range(m+1, e+1): rhs.append(nums[j])
    lhs.append(0x7fffffff)
    rhs.append(0x7fffffff)

    il, ir = 0, 0
    for i in range(b, e+1):
        if lhs[il] < rhs[ir]:
            nums[i] = lhs[il]
            il += 1
        else:
            nums[i] = rhs[ir]
            ir += 1

def test1():
    nums = [9, 8, 7, 6, 4, 3, 2, 29]
    sort(nums)
    print(nums)

def test2():
    nums = [3, 2]
    sort(nums)
    print(nums)

if __name__ == '__main__':
    test1()
    test2()
