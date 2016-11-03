"""
Given an array of random numbers. Find longest increasing subsequence (LIS) in the array.

Although this can be done in recursive and dynamic programming (DP) solutions. This should be done in O(N log N) time.

source: http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
"""
import sys
import copy

def lisNLogN(arr):
    """
    Find the longest increasing subsequence in n log n time. The basic logic is the following is that we
    create and maintain several lists of interim longest sequence.

    This is more seen as an online algorithm where each element appears and processed at a time
    as we traverse through the lists.

    There are three rules to create and maintain the interim LIS list:
        1. if arr[i] is smaller than the last element of any lists. Create a new list of len=1 contains arr[i]
        2. if arr[i] is larger than the last element of any lists. Clone and append arr[i] to the end of the
           longest list.
        3. if arr[i] is in between the largest and smallest element of any lists. Find the longest list whose
           last element is smaller than arr[i]. Clone and append arr[i] to the end of that list, 
           we will call this the new list. Discard any existing list that has the same length as the new
           list.
    """
    lists = []

    for i in xrange(len(arr)):
        # find min last element in the list
        min_end = sys.maxint
        max_end = -sys.maxint-1
        for l in lists:
            min_end = l[-1] if l[-1] < min_end else min_end
            max_end = l[-1] if max_end < l[-1] else max_end

        # case 1
        if arr[i] < min_end:
            lists.append([arr[i]])
        # case 2
        elif arr[i] > max_end:
            longest_l = max(lists, key=len)
            new_l = copy.copy(longest_l)
            new_l.append(arr[i])
            lists.append(new_l)
        # case 3
        else:
            for k in reversed(xrange(len(lists))):
                l = lists[k]
                if l[-1] < arr[i]:
                    new_l = copy.copy(l)
                    new_l.append(arr[i])
                    lists.insert(k+1, new_l)
                    if k+2 < len(lists) and len(lists[k+2]) == len(new_l):
                        lists.remove(lists[k+2])

                    break;

    return max(lists, key=len)

def test():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    rslt = lisNLogN(arr)
    assert(rslt == [0, 2, 6, 9, 11, 15])
    assert(len(rslt) == 6)

    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    rslt = lisNLogN(arr)
    assert(rslt == [1])
    assert(len(rslt) == 1)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rslt = lisNLogN(arr)
    assert(rslt == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert(len(rslt) == 10)

# run the tests
test()
print("all tests passed")
