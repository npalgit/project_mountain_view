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

def wLTwoEndBFS(beg, end, wordList):
    """
    88% performance
    """
    wordSet = set(wordList)
    if end not in wordSet: return 0
    begSet, endSet = set([beg]), set([end])
    visited = set()
    leng = 1
    while begSet and endSet:
        if len(begSet) > len(endSet):
            begSet, endSet = endSet, begSet

        temp = set()
        for word in begSet:
            chs = list(word)
            for i in range(len(chs)):
                for c in [chr( _ + ord('a')) for _ in range(26)]:
                    old_c = chs[i]
                    chs[i] = c
                    targ = ''.join(chs)
                    if targ in endSet: return leng+1
                    if targ not in visited and targ in wordSet:
                        temp.add(targ)
                        visited.add(targ)
                    chs[i] = old_c

        begSet = temp
        leng += 1

    return 0

def wLBFS(beg, end, wordList):
    """
    9% performance
    """
    wordSet = set(wordList)
    if end not in wordSet: return 0
    begSet, endSet = set([beg]), set([end])
    visited = set()
    leng = 1
    q = deque()
    q.append((beg, 1))
    while q:
        word = q.popleft()
        chs = list(word[0])
        for i in range(len(chs)):
            old_c = chs[i]
            for c in [chr( _ + ord('a')) for _ in range(26)]:
                chs[i] = c
                targ = ''.join(chs)
                if targ == end: return word[1]+1
                if targ not in visited and targ in wordSet:
                    q.append((targ, word[1]+1))
                    visited.add(targ)
            chs[i] = old_c
    return 0

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
    print(wLTwoEndBFS("hit", "cog", dic))
    print(wLBFS("hit", "cog", dic))
    print('------------------------')

def test2():
    dic = ["lamp", "himp", "rine", "limp", "lime", "like"];
    beg = "damp";
    end = "like";
    print(wL(beg, end, dic))
    print(wLSet(beg, end, dic))
    print(wLTwoEndBFS(beg, end, dic))
    print(wLBFS(beg, end, dic))
    print('------------------------')

def test3():
    dic = ["slit","bunk","wars","ping","viva","wynn","wows","irks","gang","pool","mock","fort","heel","send"]
    beg = "sand"
    end = "acne"
    print(wL(beg, end, dic))
    print(wLSet(beg, end, dic))
    print(wLTwoEndBFS(beg, end, dic))
    print(wLBFS(beg, end, dic))
    print('------------------------')

def test4():
    beg = "hit"
    end = "cog"
    dic = ["hot","dot","dog","lot","log"]
    print(wL(beg, end, dic))
    print(wLSet(beg, end, dic))
    print(wLTwoEndBFS(beg, end, dic))
    print(wLBFS(beg, end, dic))
    print('------------------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
