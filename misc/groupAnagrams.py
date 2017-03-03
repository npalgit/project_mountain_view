#!/usr/bin/python
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

leetcode #49, maybe REDO, to get familiar with python trick syntax
"""
def groupAnagrams(strs):
    d = {}

    for w in strs:
        sw = ''.join(sorted(w))
        # or below
        # sw = tuple(sorted(w))
        d[sw] = d.get(sw, []) + [w]

    return d.values()

def test1():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

if __name__ == "__main__":
    test1()
