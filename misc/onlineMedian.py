#!/usr/bin/python
"""
Find the median of incoming streams of numbers online
#295
REDDO: reimplement
"""
from heapq import *

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = []
        self.max_h = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.min_h, num)
        n = heappop(self.min_h)
        heappush(self.max_h, -n)

        if len(self.max_h) > len(self.min_h):
            n = heappop(self.max_h)
            heappush(self.min_h, -n)

    def addNumDoesNotWork(self, num):
        """
        my original does not work.
        example: [-1, -2, -3]
        """
        heappush(self.min_h, num)

        if len(self.min_h) - len(self.max_h) > 1:
            n = heappop(self.min_h)
            heappush(self.max_h, -n)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_h) == len(self.max_h):
            return (self.min_h[0] + (-self.max_h[0]))/2.0
        return float(self.min_h[0])

def test1():
    mf = MedianFinder()
    nums = [11, 13, 7, 5, 6, 1, 4, 3, 2]
    for n in nums:
        mf.addNum(n)
    print(mf.findMedian())
    print('-------------')

def test2():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())

if __name__ == '__main__':
    test1()
    test2()
