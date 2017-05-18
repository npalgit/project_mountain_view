#!/usr/bin/python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be
larger than buying price
#121
REDO: didn't figure out the trick right away. should do this very fast
"""
def bestTimeToBuySell(nums):
    int_max = 0x7fffffff
    min_v = int_max
    max_profit = 0

    for item in nums:
        if item < min_v: min_v = item
        elif item - min_v > max_profit: max_profit = item - min_v

    return max_profit

def test1():
    nums = [7, 1, 5, 3, 6, 4]
    print(bestTimeToBuySell(nums))

def test2():
    nums = [7, 6, 4, 3, 1]
    print(bestTimeToBuySell(nums))

if __name__ == '__main__':
    test1()
    test2()
