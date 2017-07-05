#!/usr/bin/python
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

#57
#REDDO: remember try not to do it in place
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    s = newInterval.start
    e = newInterval.end
    left, right = [], []

    for itm in intervals:
        if itm.end < s:
            left += itm,
        elif itm.start > e:
            right += itm,
        else:
            s = min(s, itm.start)
            e = max(e, itm.end)

    return left + [Interval(s, e)] + right


def test1():
    pass

if __name__ == '__main__':
    test1()
