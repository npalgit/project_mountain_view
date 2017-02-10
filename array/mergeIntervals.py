#!/usr/bin/python
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
leetcode #56
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def print_intervals(intervals):
    ll = []
    for i in intervals:
        ll.append([i.start, i.end])

    print(ll)

def mergeI(intervals):
    curr_idx = 0
    sor = sorted(intervals, key=lambda i:i.start)
    for i in sor:
        if i.start <= sor[curr_idx].end and sor[curr_idx].end < i.end:
            sor[curr_idx].end = i.end
        elif sor[curr_idx].end < i.start:
            curr_idx += 1
            sor[curr_idx].start = i.start
            sor[curr_idx].end = i.end

    return sor[:curr_idx+1]

def test1():
    intervals = [Interval(1,3), Interval(2, 6), Interval(8, 10), Interval(15, 18), Interval(1,9)]
    print_intervals(intervals)
    print_intervals(mergeI(intervals))

def test2():
    intervals = [Interval(1,3), Interval(2, 6), Interval(8, 10), Interval(15, 18), Interval(1,9), Interval(0, 10)]
    print_intervals(intervals)
    print_intervals(mergeI(intervals))

if __name__ == "__main__":
    test1()
    test2()
