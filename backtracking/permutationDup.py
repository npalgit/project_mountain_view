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
REDO: figure out the correct condition
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

def test1():
    nums = [1, 1, 2]
    print(permDup(nums))

def test2():
    nums = [1, 1, 1, 2]
    print(permDup(nums))

if __name__ == '__main__':
    test1()
    test2()
