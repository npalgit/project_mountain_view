#!/usr/bin/python
"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#137
REDDO: crazy smart algorithm
"""
def sn3(nums):
    """
    every element appears three times. One appears 1 or 2 times. or not multiple of 3
    """
    a = 0
    b = 0
    for c in nums:
        ta = (a&~b&~c) | (~a&b&c)
        b = (~a&b&~c) | (~a&~b&c)
        a = ta
    # view a and b each corresponding bit as counter.
    # ab, represents how many bit 1's are there.
    # if there are 1 (0b01), 2 (0b10) bits,
    # the result's corresponding bit
    # will be a 1
    return a | b # if only appears once, return b is fine

def sn4(nums):
    """
    every element appears four times. One appears 1, 2, 3 times. or not multiple of 4
    """
    a = 0
    b = 0
    for c in nums:
        ta = (a&~b&~c)|(a&b&~c)|(~a&b&c)|(a&~b&c)
        b = (~a&b&~c)|(a&b&~c)|(~a&~b&c)|(a&~b&c)
        a = ta
    # view a and b each corresponding bit as counter.
    # ab, represents how many bit 1's are there.
    # if there are 1 (0b01), 2 (0b10), 3 (0b11)  bits,
    # the result's corresponding bit
    # will be a 1
    return a | b

def test1():
    nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 9, 9]
    print(sn3(nums))

def test2():
    nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 7, 7,7, 7, 7,7, 7]
    print(sn4(nums))

if __name__ == '__main__':
    test1()
    test2()
