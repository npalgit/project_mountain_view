#!/usr/bin/python
"""
Returns a total length covered by the added intervals.
If several intervals intersect, the intersection should be
counted only once.
Example:

addInterval(3, 6)
addInterval(8, 9)
addInterval(1, 5)

getTotalCoveredLength() -> 6

i.e. [1,5) and [3,6) intersect and give a total covered interval
[1,6) with a length of 5.

[1,6) and [8,9) don't intersect, so the total covered length is a
sum of both intervals, that is 5+1=6.
     *
     *          |__|__|__|                  (3,6)
     *                         |__|         (8,9)
     *    |__|__|__|__|                     (1,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */

getTotalCoveredLength()
See insertIntervals form leetcode for various methods
"""
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# ----------------------------------------------------
class InterCov:
    """
    Uses sorting at get intervals.
    """
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        self.intervals.append(Interval(start, end))

    def getTotalCoveredLength(self):
        self.intervals.sort(cmp=lambda a, b: a.start-b.start)

        # merge
        self.merge()

        sum_val = 0
        for el in self.intervals:
            sum_val += el.end-el.start

        print([(itm.start, itm.end) for itm in self.intervals])
        return sum_val

    def merge(self):
        i = 0
        for j in range(1, len(self.intervals)):
            prev = self.intervals[i]
            curr = self.intervals[j]

            if prev.end >= curr.start:
                prev.start = min(prev.start, curr.start)
                prev.end = max(prev.end, curr.end)
            else:
                i += 1
                prev = self.intervals[i]
                prev.start = curr.start
                prev.end = curr.end

        self.intervals = self.intervals[:i+1]

# ----------------------------------------------------
class InterCovCopy:
    """
    Copying extra intervals.
    """
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        left, right = [], []

        temp_iv = Interval(start, end)
        for el in self.intervals:
            if el.end < start:
                left.append(el)
            elif el.start > end:
                right.append(el)
            else:
                temp_iv.start = min(temp_iv.start, el.start)
                temp_iv.end = max(temp_iv.end, el.end)
        self.intervals = left + [temp_iv] + right

    def getTotalCoveredLength(self):
        sum_val = 0
        for el in self.intervals:
            sum_val += el.end-el.start

        print([(itm.start, itm.end) for itm in self.intervals])
        return sum_val

# ----------------------------------------------------
class InterCovInPlace:
    """
    Doing intervals in place.
    """
    def __init__(self):
        self.intervals = []

    def addInterval(self, start, end):
        left, right = [], []
        i = 0
        inserted = False
        for j in range(len(self.intervals)):
            curr = self.intervals[j]
            if curr.end < start:
                i += 1
                continue

            elif end < curr.start and inserted:
                i += 1
                prev = self.intervals[i]
                prev.start = curr.start
                prev.end = curr.end
            elif end < curr.start and not inserted:
                self.intervals.insert(i, Interval(start, end))
                return self.intervals
            else:
                prev = self.intervals[i]
                prev.start = min(prev.start, start)
                prev.end = max(prev.end, end, curr.end)
                inserted = True

        if not inserted:
            self.intervals.append(Interval(start, end))
            return self.intervals
        self.intervals = self.intervals[:i+1]

    def getTotalCoveredLength(self):
        sum_val = 0
        for el in self.intervals:
            sum_val += el.end-el.start

        print([(itm.start, itm.end) for itm in self.intervals])
        return sum_val

def test1():
    intervals = [(3, 6), (8, 9), (1, 5)]
    cls = InterCov()
    for itm in intervals: cls.addInterval(itm[0], itm[1])
    sum_val = cls.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    intervals = [(3, 6), (8, 9), (1, 5)]
    cls2 = InterCovCopy()
    for itm in intervals: cls2.addInterval(itm[0], itm[1])
    sum_val = cls2.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    intervals = [(3, 6), (8, 9), (1, 5)]
    cls3 = InterCovInPlace()
    for itm in intervals: cls3.addInterval(itm[0], itm[1])
    sum_val = cls3.getTotalCoveredLength()
    print(sum_val)
    print('===================')

def test2():
    intervals = [[2,5], [8,12], [4, 9]]
    cls = InterCov()
    for itm in intervals: cls.addInterval(itm[0], itm[1])
    sum_val = cls.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    intervals = [[2,5], [8,12], [4, 9]]
    cls2 = InterCovCopy()
    for itm in intervals: cls2.addInterval(itm[0], itm[1])
    sum_val = cls2.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    cls3 = InterCovInPlace()
    for itm in intervals: cls3.addInterval(itm[0], itm[1])
    sum_val = cls3.getTotalCoveredLength()
    print(sum_val)
    print('===================')

def test3():
    intervals = [[1, 10], [1, 3], [2, 6], [8, 10], [15, 18], [19, 22], [8, 17]]
    cls = InterCov()
    for itm in intervals: cls.addInterval(itm[0], itm[1])
    sum_val = cls.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    intervals = [[1, 10], [1, 3], [2, 6], [8, 10], [15, 18], [19, 22], [8, 17]]
    cls2 = InterCovCopy()
    for itm in intervals: cls2.addInterval(itm[0], itm[1])
    sum_val = cls2.getTotalCoveredLength()
    print(sum_val)
    print('--------------------')
    cls3 = InterCovInPlace()
    for itm in intervals: cls3.addInterval(itm[0], itm[1])
    sum_val = cls3.getTotalCoveredLength()
    print(sum_val)
    print('===================')

if __name__ == '__main__':
    test1()
    test2()
    test3()
