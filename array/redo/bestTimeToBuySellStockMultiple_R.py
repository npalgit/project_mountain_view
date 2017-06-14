#!/usr/bin/python
"""
Say you have an array for which the ith element is the price of
a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as
many transactions as you like (ie, buy one and sell one share of the
stock multiple times). However, you may not engage in multiple
transactions at the same time (ie, you must sell the stock before
you buy again).
#122
REDDO: figure out the rule fast
"""
def bestTimeToBuySellMultiple(nums):
    max_prof = 0
    local_min = nums[0]
    local_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            local_min = nums[i]
        #elif nums[i] > nums[i-1]:
        local_max = nums[i]
        max_prof = max(max_prof, local_max-local_min)

    return max_prof

def bestTimeToBuySellMultipleSimple(nums):
    max_prof = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            max_prof += nums[i]-nums[i-1]

    return max_prof

def test1():
    nums = [7, 1, 5, 3, 6, 4, 4, 4]
    print(bestTimeToBuySellMultiple(nums))
    print(bestTimeToBuySellMultipleSimple(nums))

if __name__ == '__main__':
    test1()

