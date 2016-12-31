#!/usr/bin/python
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

leetcode #3
REDO for better practice.
"""

def longestNonRepeatingSubstring(str):
    """
    Solution time complexity O(n), space complexity O(n).
    """

    dic = {}
    i = 0
    max_len = 0

    for j in xrange(len(str)):
        v = str[j]
        if v in dic:
            i = max(dic[v] + 1, i)

        tmp = j-i+1
        if tmp > max_len:
            max_len = tmp

        dic[v] = j

    return max_len

def test1():
    str = "abcabcbb"
    print(longestNonRepeatingSubstring(str))

def test2():
    str = "bbbbbbbb"
    print(longestNonRepeatingSubstring(str))

def test3():
    str = "pwwkew"
    print(longestNonRepeatingSubstring(str))

def test4():
    str = "ababababababcdeababab"
    print(longestNonRepeatingSubstring(str))

def test5():
    str = "abba"
    print(longestNonRepeatingSubstring(str))

def test6():
    str = "tmmzuxt"
    print(longestNonRepeatingSubstring(str))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
