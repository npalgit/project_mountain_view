#!/usr/bin/python
import sys

def find_array_product_except_one(arr):
    """
    Find the array product except for one entry using O(n) time and O(1) space.
    Solution is O(n) speed and O(n) space.
    """
    if len(arr) == 1:
        return None

    # corner case when arr is 1 or 2.
    l = [None]*len(arr)
    r = [None]*len(arr)
    l[0] = 1
    r[len(arr)-1] = 1

    for i in xrange(1, len(arr)):
        l[i] = arr[i-1]*l[i-1]

    for j in reversed(xrange(0, len(arr)-1)):
        r[j] = arr[j+1]*r[j+1]

    # find max by l[k]*r[k], whatever k index is the largest.
    max = r[0]*l[0]

    for k in xrange(1, len(arr)):
        tmp = l[k]*r[k]
        if tmp > max:
            max = tmp
    return max

def find_array_product_except_one_constant_space(arr):
    """
    Find the array product except for one entry using O(n) time and O(1) space. The logic is the following:

    condition 1: even negative, ignore the smallest postive integer
    condition 2: odd negative, ignore the largest negative integer, smallest abs(neg integer)
    condition 3: all negative and total number of elements even, ignore the largest abs(negative integer)
                 or smallest negative integer
                 all negative and total number of elements odd, ignore the smalles abs(neg integer) or largest
                  neg integer
    condition 4: all positive, ignore the smallest integer
    go through once, keep track, the smallest pos integer, largest neg integer, smallest neg integer,
    also keep track of number of negative integer
    """

    if len(arr) <= 1:
        return None

    min_int = -sys.maxint-1
    max_neg = (min_int, -1)
    min_neg = (1, -1)
    min_pos = (sys.maxint, -1)
    num_neg = 0

    for i in xrange(len(arr)):
        # keep track of negative integers
        if arr[i] < 0:
            num_neg += 1

            if arr[i] < min_neg[0]:
                min_neg = (arr[i], i)
            if arr[i] > max_neg[0]:
                max_neg = (arr[i], i)
        else:
            if arr[i] < min_pos[0]:
                min_pos = (arr[i], i)

    mul = 1
    # condition 3 all negative, but odd number elements
    if num_neg == len(arr) and num_neg%2 == 1:
        ign_idx = max_neg[1]
    elif num_neg == len(arr) and num_neg%2 == 0:
        ign_idx = min_neg[1]
    # condition 4, only positive integers
    elif num_neg == 0:
        ign_idx = min_pos[1]
    # condition 2
    elif num_neg%2 == 1:
        ign_idx = max_neg[1]
    # condition 1
    elif num_neg%2 == 0:
        ign_idx = min_pos[1]

    for i in xrange(len(arr)):
        if i != ign_idx:
            mul *= arr[i]
    return mul

def test1():
    arr = [3, 2, -1, 4, -1, 6]
    print(find_array_product_except_one(arr))
    print(find_array_product_except_one_constant_space(arr))

    arr = [5, 12, -1, -1, 1, 6, -3]
    print(find_array_product_except_one(arr))
    print(find_array_product_except_one_constant_space(arr))

    arr = [-1, -2, -3, -4, -5, -6]
    print(find_array_product_except_one(arr))
    print(find_array_product_except_one_constant_space(arr))

    arr = [4]
    print(find_array_product_except_one(arr))
    print(find_array_product_except_one_constant_space(arr))

if __name__ == '__main__':
    test1()
