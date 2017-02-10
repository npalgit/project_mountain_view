#!/usr/bin/python
"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
leetcode #14
"""
def longestCommonPrefix(ll):

    if ll is None or len(ll) == 0:
        return ""

    sub_s = ll[0]
    for l in ll[1:]:
        s = 0
        while s < min(len(sub_s), len(l)) and sub_s[s] == l[s]:
            s += 1

        sub_s = sub_s[:s]

    return sub_s

def test1():
    ll = ['leetcodeabc', 'leetcode', 'leeka', 'leet', 'leebsd']
    print(longestCommonPrefix(ll))

def test2():
    ll = ['abc', 'def', 'ghi']
    print(longestCommonPrefix(ll))

def test3():
    ll = ['abc', 'hello', 'hello']
    print(longestCommonPrefix(ll))

def test4():
    ll = ['leb', 'leet', 'leetcode', 'lees']
    print(longestCommonPrefix(ll))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
