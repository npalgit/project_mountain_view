#!/usr/bin/python
"""
Given a string S and a string T, find the minimum window in S which will contain all
the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.

#76
REDO: must get slide window first try
"""

def minWindowSlideWin(s, t):
    """
    68.8% performance
    """
    mp = [0]*128
    cnt = 0
    set_t = set(list(t))
    win_s = len(s)+1
    get_idx = lambda c: ord(c)
    for c in t: mp[get_idx(c)] += 1
    left, right = 0, 0
    hd = 0

    for right in range(len(s)):
        if s[right] in set_t:
            mp[get_idx(s[right])] -= 1
            if mp[get_idx(s[right])] >= 0:
                cnt += 1

        while cnt == len(t):
            if right-left+1 < win_s:
                win_s = right-left + 1
                hd = left

            if s[left] in set_t:
                mp[get_idx(s[left])] += 1
                if mp[get_idx(s[left])] > 0:
                    cnt -= 1

            left += 1

    return '' if win_s == len(s)+1 else s[hd:hd+win_s]

def minWindow(s, t):
    """
    TLE with 267/268 accepted.
    """
    min_win_s = len(s)
    win_subs = ''
    w_dic = {}
    for i in range(len(s)-len(t)+1):
        for c in t: w_dic[c] = w_dic.get(c, 0) + 1

        for j in range(min_win_s):
            if i+j < len(s) and s[i+j] in w_dic:
                w_dic[s[i+j]] -= 1
                if w_dic[s[i+j]] == 0: del w_dic[s[i+j]]

            if not w_dic:
                min_win_s = j+1
                win_subs = s[i:i+j+1]
                break

        w_dic.clear()

    return win_subs

def test1():
    s = 'ADOBECODEBANCDDD'
    t = 'ABC'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print('----------------')

def test2():
    s = 'ADOBECODEBANCDDD'
    t = 'XYZ'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print('----------------')

def test3():
    s = ''
    t = 'ABC'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print('----------------')

def test4():
    s = ''
    t = ''
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print('----------------')

def test5():
    s = 'a'
    t = 'a'
    print(minWindow(s, t))
    print(minWindowSlideWin(s, t))
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
