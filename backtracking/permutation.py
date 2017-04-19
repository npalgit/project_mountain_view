#!/usr/bin/python
"""
Generate all permutations for a list of numbers.
#46
"""
def perm(nums):
    lists = []
    dfs(lists, [], nums)
    return lists

def dfs(lists, l, nums):
    if len(l) == len(nums):
        lists.append(list(l))
        return
    for n in nums:
        if n not in l:
            l.append(n)
            dfs(lists, l, nums)
            l.pop()

def permute90(self, nums):
    """
    Performance in the 90%+ range. Not using recursion
    """
    ans = [nums]
    for i in xrange(1, len(nums)):
        m = len(ans)
        for k in xrange(m):
            for j in xrange(i):
                ans.append(ans[k][:])
                ans[-1][j], ans[-1][i] = ans[-1][i], ans[-1][j]
    return ans

def perm_set(nums):
    """
    leetcode slower than normal lists. But theoretically it should be faster.
    """
    from collections import OrderedDict
    lists = []
    s = OrderedDict()
    dfs_set(lists, s, nums)
    return lists

def dfs_set(lists, s, nums):
    if len(s) == len(nums):
        lists.append(list(s))
        return
    for n in nums:
        if n not in s:
            s[n] = None
            dfs_set(lists, s, nums)
            s.popitem()

def test1():
    nums = [1, 2, 3]
    print(perm_set(nums))

def test2():
    nums = [4, 3, 2, 1]
    print(perm_set(nums))

if __name__ == '__main__':
    test1()
    test2()
