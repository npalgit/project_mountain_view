#!/usr/bin/python
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
import sys

def shortest_palindrome_parition_top_down(str):
    return recursive_partition(str, 0, len(str)-1)

def isPali(str, beg, end):
    i = beg
    j = end
    while (i <= j):
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1

    return True

def recursive_partition(str, beg, end):
    if beg > end:
        return 0
    if beg == end:
        return 1
    if isPali(str, beg, end):
        return 1

    min_part = sys.maxint

    for i in xrange(beg, end):
        lhs = recursive_partition(str, beg, i)
        rhs = recursive_partition(str, i+1, end)

        if lhs + rhs <  min_part:
            min_part = lhs + rhs

    return min_part

def shortest_palindrome_parition_dp(str):
    pass

if __name__ == '__main__':
    arr = ['a', 'b', 'a', 'b', 'a', 'd', 'e', 'd']
    print(shortest_palindrome_parition_top_down(arr))

    arr = ['a', 'b', 'a', 'b']
    print(shortest_palindrome_parition_top_down(arr))

    arr = ['a', 'b', 'c']
    print(shortest_palindrome_parition_top_down(arr))

    arr = ['e', 'b', 'c', 'b', 'a', 'b', 'c', 'b', 'a']
    print(shortest_palindrome_parition_top_down(arr))
  
