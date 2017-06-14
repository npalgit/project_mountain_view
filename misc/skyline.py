#!/usr/bin/python
"""
The skyline problem.
buildings are denoted as [Li, Ri, Hi] for example: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
return: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
#218
REDO
"""

from heapq import *
def getSkyline(buildings):
    """
    TLE with 35/36 passed. Same code in java also TLE with 36/36.
    Implementation with TreeMap in java passes with 68.8%
    """
    bds = []
    heap = [] # assume max heap, then work around
    isBeg = lambda x: x[1] < 0
    peek = lambda heap: abs(heap[0])
    getHeight = lambda x: abs(x[1])
    getIdx = lambda x: x[0]

    for i in buildings:
        bds.append((i[0], -i[2]))
        bds.append((i[1], i[2]))
    bds.sort(cmp=cmp)

    heappush(heap, 0)
    res = []
    prev = 0
    for bd in bds:
        if isBeg(bd):
            heappush(heap, -getHeight(bd))
        else:
            heap.remove(-getHeight(bd))
            heapify(heap)

        curr = peek(heap)
        if curr != prev:
            res.append((getIdx(bd) , curr))
            prev = curr

        #if isBeg(bd):
        #    if getHeight(bd) > peek(heap):
        #        heappush(heap, -getHeight(bd))
        #        res.append((getIdx(bd), getHeight(bd)))
        #    else:
        #        heappush(heap, -getHeight(bd))

        #else:
        #    if getHeight(bd) == peek(heap):
        #        heappop(heap)
        #        res.append((getIdx(bd), peek(heap)))
        #    elif -getHeight(bd) in heap:
        #        heap.remove(-getHeight(bd))
    return res

def cmp(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return a[0] - b[0]

def test1():
    buildings =[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(getSkyline(buildings))

def test2():
    buildings = [[1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 7, 4], [8, 9, 4]]
    print(getSkyline(buildings))

def test3():
    buildings = [[0, 1, 2], [0, 2, 3], [3, 5, 3], [4, 5, 2], [6, 7, 2], [7, 8, 3]]
    print(getSkyline(buildings))

def test4():
    buildings = [[1, 3, 4], [3, 4, 4], [2, 6, 2], [8, 11, 4], [7, 9, 3],[10, 11, 2]]
    print(getSkyline(buildings))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
