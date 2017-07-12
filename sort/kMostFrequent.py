#!/usr/bin/python
"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
Order does not matter.
#347
REDO: go over algorithm no need to code everything. look into bucket sort
"""
from Queue import PriorityQueue
from heapq import *

def kMostFreqSelect(nums, k):
    """
    make sure data is returned in order, largest first.
    the problem does not specify this. So this can be simplified a lot more.
    """
    cnts = {}
    for i in nums:
        cnts[i] = cnts.get(i, 0)+1

    cnts = cnts.items()
    res = []
    b, e = 0, len(cnts)-1
    for i in reversed(range(k)):
        mid = partition(cnts, b, e, i)
        res.append(cnts[mid][0])
        e = mid -1
    return res[::-1]

def partition(nums, b, e, k):
    if b > e:
        return

    i = b-1
    pivot = nums[e][1]

    for j in range(b, e):
        if nums[j][1] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[e] = nums[e], nums[i+1]
    mid = i+1
    if mid == k:
        return mid
    if k < mid:
        return partition(nums, b, mid-1, k)
    else:
        return partition(nums, mid+1, e, k)

def kMostFreqSelectUnordered(nums, k):
    """
    returned data is no ordered
    """
    cnts = {}
    for i in nums:
        cnts[i] = cnts.get(i, 0)+1

    cnts = cnts.items()
    b, e = 0, len(cnts)-1
    return [itm[0] for itm in partition2(cnts, b, e, k-1)]

def partition2(nums, b, e, k):
    if b > e:
        return

    i = b-1
    pivot = nums[e][1]

    for j in range(b, e):
        if nums[j][1] >= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[e] = nums[e], nums[i+1]
    mid = i+1
    if mid == k:
        return nums[:mid+1]
    if k < mid:
        return partition2(nums, b, mid-1, k)
    else:
        return partition2(nums, mid+1, e, k)

def kMostFreqHeapThreePass(nums, k):
    freq = {}
    heap = PriorityQueue(k)
    # count
    for i in nums: freq[i] = freq.get(i, 0)+1
    for key, val in freq.iteritems():
        if not heap.full():
            heap.put((val, key))
        else:
            if heap.queue[0][0] < val:
                heap.get()
                heap.put((val, key))

    return [itm[1] for itm in reversed(heap.queue)]

def kMostFreqHeapOnline(nums, k):
    """
    Constantly maintaining a heap. TLE at 19/2
    """
    dic = {}
    pq = []

    peek = lambda q : q[0]
    for v in nums:
        node = dic.get(v, [0, v, False])
        node[0] += 1
        dic[v] = node
        heapify(pq)

        if len(pq) < k:
            if node[2] == False:
                node[2] = True
                heappush(pq, node)
        else:
            if node[2] == False and node[0] > peek(pq)[0]:
                old_n = heappop(pq)
                old_n[2] = False
                node[2] = True
                heappush(pq, node)
    res = []

    while pq:
        res.append(heappop(pq)[1])

    res.reverse()
    return res

def test1():
    nums = [1, 1, 2, 2, 3, 4,4,4, 4,  5, 6, 7, 8]
    print(kMostFreqHeapThreePass(nums, 3))
    nums = [1, 1, 2, 2, 3, 4,4,4, 4,  5, 6, 7, 8]
    print(kMostFreqSelectUnordered(nums, 3))

if __name__ == '__main__':
    test1()
