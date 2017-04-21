#!/usr/bin/python
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
#11
"""
def mostW(h):
    max_area = 0
    i, j = 0, len(h)-1
    while i < j:
        curr_area = (j-i)*min(h[i], h[j])
        max_area = max(max_area, curr_area)
        if h[i] < h[j]:
            i += 1
        else:
            j -= 1

    return max_area

def test1():
    h = [1, 6, 2, 8, 5, 4]
    print(mostW(h))

if __name__ == '__main__':
    test1()
