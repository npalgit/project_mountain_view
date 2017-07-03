#!/usr/bin/python
"""
Generate all permutations for a list of numbers that may have duplicates.

[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

#47
REDDO: figure out the correct condition
review: interesting condition to track
"""
def permDup(nums):
    lists = []
    nums.sort()
    used = [False]*len(nums)
    dfs(lists, [], used,  nums)
    return lists

def dfs(lists, l, used, nums):
    if len(l) == len(nums):
        lists.append(list(l))
        return

    for i in range(len(nums)):
        if used[i] or i >0 and nums[i] == nums[i-1] and not used[i-1]: continue

        used[i] = True
        l.append(nums[i])
        dfs(lists, l, used, nums)
        used[i] = False
        l.pop()

def permDup_r(nums):
    used = [False]*len(nums)
    trace = []
    res = []
    dfs_r(nums, trace, used, res)
    return res

def dfs_r(nums, trace, used, res):
    if len(trace) == len(nums):
        res.append(list(trace))
        return

    for i in range(len(nums)):
        if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
            continue
        used[i] = True
        trace.append(nums[i])
        dfs_r(nums, trace, used, res)
        trace.pop()
        used[i] = False

def test1():
    nums = [1, 1, 2]
    print(permDup(nums))
    print(permDup_r(nums))
    print('--------------')

def test2():
    nums = [1, 1, 1, 2]
    print(permDup(nums))
    print(permDup_r(nums))
    print('--------------')

if __name__ == '__main__':
    test1()
    test2()
