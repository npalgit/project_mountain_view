#!/usr/bin/python
"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
#40
REDDO: good structure for backtracking. redo with dp
"""
def comboSumDup(targ, nums):
    """
    50% to 28% range, not terribly fast.
    """
    nums.sort()
    lists = []
    dfs(lists, [], targ, 0, nums)
    return lists

def dfs(lists, l, rem, start, nums):
    if rem < 0: return
    if rem == 0:
        lists.append(list(l))
        return

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]: continue
        l.append(nums[i])
        dfs(lists, l, rem-nums[i], i+1, nums)
        l.pop()

def test1():
    targ = 8
    nums = [1, 10, 1, 2, 7, 6, 1, 5]
    print(comboSumDup(targ, nums))
    print('----------------')

def test2():
    targ = 10
    nums = [2, 2, 3, 6, 7]
    print(comboSumDup(targ, nums))
    print('----------------')


if __name__ == '__main__':
    test1()
    test2()
