#!/usr/bin/python
"""
Given a set of distinct integers, nums, return all possible subsets permutaiton
#??
"""
def subset_permutation(nums):
    lists = []
    dfs(lists, [], nums)
    return lists

def dfs(lists, l, nums):
    if len(l) > len(nums): return
    if l: lists.append(list(l))

    for n in nums:
        if n not in l:
            l.append(n)
            dfs(lists, l, nums)
            l.pop()

def test1():
    nums = [1, 2, 3]
    print(subset(nums))
    print('---------------')

def test2():
    nums = [1, 2, 3, 4]
    print(subset(nums))

if __name__ == '__main__':
    test1()
    test2()
