#!/usr/bin/python
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

#253
REDO2: great problem to review
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def numRoom(intervals):
    beg = []
    end = []
    for itm in intervals:
        beg.append(itm[0])
        end.append(itm[1])
    beg.sort()
    end.sort()
    i, j = 0, 0
    curr_num, max_num = 0, 0
    while i < len(beg):
        if beg[i] < end[j]:
            curr_num += 1
            max_num = max(curr_num, max_num)
            i += 1
        else:
            curr_num -= 1
            j += 1

    return max_num

def test1():
    times = [[0, 30],[5, 10],[15, 20]]
    print(numRoom(times))

def test2():
    times = [[1, 4], [1, 2], [4, 9], [6, 10], [13, 15]]
    print(numRoom(times))

def test3():
    times = []
    print(numRoom(times))

def test4():
    times = [[3, 4]]
    print(numRoom(times))

def test5():
    times = [[2, 11], [6, 16], [11, 16]]
    print(numRoom(times))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
