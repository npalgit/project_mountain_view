#!/usr/bin/python
"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
#179

REDO: quickly briefly know how to implement
"""
def largestNumbers(nums):
    s_nums = [str(n) for n in nums]
    cmp_func = lambda s1, s2: -1 if s1+s2 > s2+s1 else (1 if s1+s2 < s2+s1 else 0)
    s_nums.sort(cmp=cmp_func)
    return str(int(''.join(s_nums)))

def test1():
    nums = [3, 30, 34, 5, 9]
    print(largestNumbers(nums))

def test2():
    nums = [0, 0, 0, 0]
    print(largestNumbers(nums))

if __name__ == '__main__':
    test1()
    test2()
