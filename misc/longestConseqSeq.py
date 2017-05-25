#!/usr/bin/python
"""
Given an unsorted array of integers, find the length of the longest consecutive elements
sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

#128
REDO: unique algo never seen before, know both algos
"""
def findLongest(nums):
    dic = {}
    res = 0
    for n in nums:
        if n not in dic:
            left = dic.get(n-1, 0)
            right = dic.get(n+1, 0)
            sum = left + right + 1
            res = max(res, sum)
            dic[n] = sum

            dic[n-left] = sum
            dic[n+right] = sum

    return res

def findLongestSet(nums):
    """
    more concise and faster solution
    """
    s = set(nums)
    res = 0
    for x in s:
        if x-1 not in s:
            y = x+1
            while y in s:
                y += 1
            res = max(res, y-x)

    return res

def test1():
    nums = [100, 4, 200, 1, 3, 2]
    print(findLongest(nums))
    print(findLongestSet(nums))

if __name__ == '__main__':
    test1()
