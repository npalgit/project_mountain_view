#!/usr/bin/python
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

#438
"""

def allAnagram(s, p):
    """
    99.48% but corner case so annoying.
    """
    win_s = len(p)
    if len(s) < win_s: return []
    res = []
    hist = {}

    count = 0
    # preprocess
    for c in p:
        hist[c] = hist.get(c, 0) + 1
    for i in range(win_s):
        if s[i] in hist:
            hist[s[i]] -= 1
            if hist[s[i]] >= 0:
                count += 1
    if count == win_s:
        res.append(0)

    for i in range(win_s, len(s)):
        # in
        if s[i] in hist:
            hist[s[i]] -= 1
            if hist[s[i]] >= 0:
                count += 1

        # out
        if s[i-win_s] in hist:
            hist[s[i-win_s]] += 1
            if hist[s[i-win_s]] > 0:
                count -= 1
        if count == win_s: res.append(i-win_s+1)

    return res

def test1():
    s = "cbaebabacd"
    p = "abc"
    print(allAnagram(s, p))

def test2():
    s = "abab"
    p = "ab"
    print(allAnagram(s, p))

def test4():
    s = 'aaaaaaaaaaaaaaaaaaaaaab'
    p = 'ab'
    print(allAnagram(s, p))

def test3():
    s = "ababaaaaaaaaaaabcaaaaaaaaaabc"
    p = "abc"
    print(allAnagram(s, p))

def test4():
    s = 'baa'
    p = 'aa'
    print(allAnagram(s, p))

def test5():
    s = 'pbaa'
    p = 'aa'
    print(allAnagram(s, p))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
