#!/usr/bin/python
#126
from collections import deque

def wL(beg, end, dic):
    """
    TLE 19/39 passed
    """
    dic_set = set(dic)
    q = deque()
    q.append((beg, [beg], 1, dic_set))
    rslt = []
    min_len = len(dic)

    while q:
        n = q.popleft()
        dic_set = n[3]

        for itm in dic_set:
            word = n[0]
            l = n[1]
            level = n[2]

            if cmpStr(word, itm):
                if itm == end and min_len == len(dic):
                    min_len = level+1

                if itm == end and min_len == level+1:
                    l.append(itm)
                    rslt.append(l)
                    continue

                new_l = list(l)
                new_l.append(itm)

                dic_set_cp = dic_set.copy()
                dic_set_cp.remove(itm)
                q.append((itm, new_l, level+1, dic_set_cp))

    return rslt

def cmpStr(s1, s2):
    diffCnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: diffCnt += 1
        if diffCnt > 1: return False

    return True if diffCnt == 1 else False

def test1():
    beg = "hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(wL(beg, end, wordList))

def test2():
    beg = "red"
    end = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    print(wL(beg, end, wordList))

if __name__ == '__main__':
    test1()
    test2()

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
