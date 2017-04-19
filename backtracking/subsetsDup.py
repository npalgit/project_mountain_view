#!/usr/bin/python
"""
Given a set of distinct integers, nums, return all possible subsets permutation
#90
"""
def subsetsDup(nums):
    lists = []
    nums.sort()
    dfs(lists, [], nums, 0)
    return lists

def dfs(lists, l, nums, start):
    lists.append(list(l))

    for i in range(start, len(nums)):
        if i > start and nums[i-1] == nums[i]:
            continue

        l.append(nums[i])
        dfs(lists, l, nums, i+1)
        l.pop()

def test1():
    nums = [1, 2, 2]
    print(subsetsDup(nums))
    print('---------------')

def test2():
    nums = [1, 2, 2, 2, 3, 3, 4]
    print(subsetsDup(nums))

if __name__ == '__main__':
    test1()
    test2()
