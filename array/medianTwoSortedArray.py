#!/usr/bin/python
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
leetcode #4
REDDO this problem
"""
def medianTwoSortedArrays(A, B):
    m, n = len(A), len(B)
    # make sure A is shorter than B
    if m > n:
        m, n, A, B = n, m, B, A
    if n == 0:
        raise ValueError

    i_min, i_max = 0, m
    half_len = (m+n+1)/2

    while i_min <= i_max:
        i = (i_min + i_max)/2
        j = half_len - i

        if i < m and B[j-1] > A[i]:
            i_min = i + 1
        elif i > 0 and A[i-1] > B[j]:
            i_max = i - 1
        else:
            if i == 0: max_left = B[j-1]
            elif j == 0: max_left = A[i-1]
            else: max_left = max(A[i-1], B[j-1])

            if (m+n)%2 == 1:
                return max_left

            if i == m: min_right = B[j]
            elif j == n: min_right = A[i]
            else: min_right = min(A[i], B[j])

            return (max_left + min_right)/2.0

def medianWB(n1, n2):
    """
    Note: this is for equal length
    """
    if not n1 and not n2: return None

    if not n1 or not n2:
        n = n1 if not n2 else n2
        return getMedian(n)[1]

    while len(n1) >= 2 and len(n2) >= 2:
        m1, m2 = getMedian(n1), getMedian(n2)

        if m1[1] == m2[1]:
            return m1[1]

        if m1[1] > m2[1]:
            n1, n2 = n2, n1
            m1, m2 = m2, m1

        n1 = n1[m1[0]:] if len(n1)%2 == 1 else n1[m1[0]+1:]
        n2 = n2[:m2[0]+1]

    if len(n1) == 1 and len(n2) == 1:
        return (n1[0]+n2[0])/2.0
    elif len(n1) == 2 or len(n2) == 2:
        concat_n = n1 + n2
        return sum(concat_n) - max(concat_n) - min(concat_n)

def getMedian(n):
    mid = (len(n)-1)/2
    if len(n)%2 == 1:
        return (mid, n[mid])
    else:
        return (mid, (n[mid]+n[mid+1])/2.0)

def test1():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(medianTwoSortedArrays(arr1, arr2))
    print(medianWB(arr1, arr2))

def test2():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8]
    print(medianTwoSortedArrays(arr1, arr2))
    print(medianWB(arr1, arr2))

def test3():
    arr1 = [3, 8, 9]
    arr2 = [4, 5, 6]
    print(medianTwoSortedArrays(arr1, arr2))
    print(medianWB(arr1, arr2))

def test4():
    arr1 = [1, 20]
    arr2 = [3, 4, 5, 6, 7]
    print(medianTwoSortedArrays(arr1, arr2))
    print(medianWB(arr1, arr2))

if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    test4()
