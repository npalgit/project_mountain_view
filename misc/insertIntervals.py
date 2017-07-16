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

def insertInPlace(intervals, newInterval):
    """
    Accepted 42.11%
    """
    i = 0
    inserted = False
    start, end = newInterval.start, newInterval.end
    for j in range(len(intervals)):
        curr = intervals[j]
        if curr.end < start:
            i += 1
            continue

        elif end < curr.start and inserted:
            i += 1
            prev = intervals[i]
            prev.start = curr.start
            prev.end = curr.end
        elif end < curr.start and not inserted:
            intervals.insert(i, Interval(start, end))
            return intervals
        else:
            prev = intervals[i]
            prev.start = min(prev.start, start)
            prev.end = max(prev.end, end, curr.end)
            inserted = True

    if not inserted:
        intervals.append(Interval(start, end))
        return intervals
    return intervals[:i+1]

def insertInPlaceDeletion(intervals, newInterval):
    """
    28.52% accepted
    """
    iStart, iEnd = newInterval.start, newInterval.end
    i = 0
    inserted = False
    while i < len(intervals):
        prev = intervals[i]
        if prev.end < iStart:
            i += 1
        elif iEnd < prev.start:
            inserted = True
            intervals.insert(i, Interval(iStart, iEnd))
            break
        else:
            # modify in place
            iStart = min(prev.start, iStart)
            iEnd = max(prev.end, iEnd)
            intervals.remove(prev)

    if not inserted:
        intervals.append(Interval(iStart, iEnd))
    return intervals

def test1():
    nums = [[1, 2], [4, 5], [6, 8], [9, 10], [15, 20]]
    newInterval = Interval(5, 9)
    intervals = map(lambda n: Interval(n[0], n[1]), nums)
    res = insertInPlaceDeletion(intervals, newInterval)
    print(map(lambda n: (n.start, n.end), res))

def test2():
    nums = [[4, 5], [6, 8]]
    newInterval = Interval(1, 2)
    intervals = map(lambda n: Interval(n[0], n[1]), nums)
    res = insertInPlaceDeletion(intervals, newInterval)
    print(map(lambda n: (n.start, n.end), res))

def test3():
    nums = [[1, 2], [4, 5]]
    newInterval = Interval(8, 9)
    intervals = map(lambda n: Interval(n[0], n[1]), nums)
    res = insertInPlaceDeletion(intervals, newInterval)
    print(map(lambda n: (n.start, n.end), res))

def test4():
    nums = [[1, 2], [8, 9]]
    newInterval = Interval(4, 5)
    intervals = map(lambda n: Interval(n[0], n[1]), nums)
    res = insertInPlaceDeletion(intervals, newInterval)
    print(map(lambda n: (n.start, n.end), res))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
