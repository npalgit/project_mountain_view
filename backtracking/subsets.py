#!/usr/bin/python
"""
Given a set of distinct integers, nums, return all possible subsets permutaiton
#78
"""
def subset(nums):
    lists = []
    dfs(lists, [], nums)
    return lists

def dfs(lists, l, nums):
    if len(l) > len(nums): return
    lists.append(list(l))

    for n in nums:
        if not l or n > l[-1]:
            l.append(n)
            dfs(lists, l, nums)
            l.pop()

def subset2(nums):
    lists = []
    dfs2(lists, [], nums, 0)
    return lists

def dfs2(lists, l, nums, start):
    lists.append(list(l))

    for i in range(start, len(nums)):
        l.append(nums[i])
        dfs2(lists, l, nums, i+1)
        l.pop()

def test1():
    nums = [1, 2, 3]
    print(subset2(nums))
    print('---------------')

def test2():
    nums = [1, 2, 3, 4]
    print(subset2(nums))

if __name__ == '__main__':
    test1()
    test2()
