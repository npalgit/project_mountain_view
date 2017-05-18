#!/usr/bin/python
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
#88
"""
def merge(nums1, m, nums2, n):
    end = m+n-1
    i, j = m-1, n-1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[end] = nums1[i]
            i -= 1
        else:
            nums1[end] = nums2[j]
            j -= 1

        end -= 1

    while j >= 0:
        nums1[end] = nums2[j]
        end -= 1
        j -= 1

    return nums1

def test1():
    n1 = [3, 5, 9, 13, 14]
    n2 = [1, 2, 4, 8, 12, 13]
    m, n = len(n1), len(n2)
    n1.extend([0]*len(n2))
    print(n1)
    print(n2)
    print(merge(n1, m, n2, n))

if __name__ == '__main__':
    test1()
