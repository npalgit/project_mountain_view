#!/usr/bin/python
from collections import deque
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

#127
"""

def wL(beg, end, dic):
    visited = [False]*len(dic)
    q = deque()
    q.append((beg, 1))
    while q:
        w = q.popleft()
        for idx, itm in enumerate(dic):
            if not visited[idx] and cmpStr(w[0], itm):
                if itm == end:
                    return w[1]+1
                q.append((itm, w[1]+1))
                visited[idx] = True

    return 0

def wLSet(beg, end, dic):
    """
    Similar solution submitted and accepted in java. Superslow 5.96% speed.
    """
    dic_set = set(dic)
    q = deque()
    q.append((beg, 1))
    while q:
        w = q.popleft()
        for itm in dic_set.copy():
            if cmpStr(w[0], itm):
                if itm == end:
                    return w[1]+1
                q.append((itm, w[1]+1))
                dic_set.remove(itm)

    return 0

def cmpStr(s1, s2):
    diffCnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: diffCnt += 1
        if diffCnt > 1: return False

    return True if diffCnt == 1 else False

def test1():
    dic = ["hot", "hik", "dot", "dog","lot","log","cog"]
    print(wL("hit", "cog", dic))
    print(wLSet("hit", "cog", dic))

def test2():
    dic = ["lamp", "himp", "rine", "limp", "lime", "like"];
    beg = "damp";
    end = "like";
    print(wL(beg, end, dic))
    print(wLSet(beg, end, dic))

def test3():
    dic = ["slit","bunk","wars","ping","viva","wynn","wows","irks","gang","pool","mock","fort","heel","send"]
    beg = "sand"
    end = "acne"
    print(wL(beg, end, dic))
    print(wLSet(beg, end, dic))

if __name__ == '__main__':
    test1()
    test2()
    test3()
