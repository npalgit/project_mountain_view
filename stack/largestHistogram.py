#!/usr/bin/python
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
#84
REDO: related to 42, make sure can do both solutions and know the difference
"""
def largHist2(height):
    max_ar = 0
    i = 0
    s = []
    while i < len(height):
        if not s or height[i] >= height[s[-1]]:
            s.append(i)
            i += 1
        else:
            h = height[s.pop()]
            w = i - s[-1]-1 if s else i
            max_ar = max(max_ar, h*w)
    while s:
        h = height[s.pop()]
        w = i - s[-1]-1 if s else i
        max_ar = max(max_ar, h*w)

    return max_ar

def largHist(height):
    height.append(0)
    s = [-1]
    max_ar = 0
    for i in range(len(height)):
        while height[i] < height[s[-1]]:
            h = height[s.pop()]
            w = i - s[-1]-1
            max_ar = max(max_ar, h*w)
        s.append(i)
    return max_ar

def histogram_r(heights):
    heights = [-1] + heights + [0]
    max_area = 0
    stck = []
    stck.append(0)
    for curr in range(1, len(heights)):
        while heights[curr] <= heights[stck[-1]]:
            h = heights[stck.pop()]
            w = curr-stck[-1]-1
            max_area = max(max_area, h*w)

        stck.append(curr)

    return max_area

def test1():
    height = [2, 1, 5, 6, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]
    print(largHist(height))
    print(largHist2(height))
    print('------------------')

def test2():
    height = [2, 2, 2]
    print(largHist(height))
    print(largHist2(height))
    print('------------------')

if __name__ == '__main__':
    test1()
    test2()
