#!/usr/bin/python
"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]
#30
"""
def findSubstr(s, words):
    """
    TLE with 168/169 test cases passed.
    """
    rslt = []
    w_len = len(words[0])
    i = 0
    while i <= len(s)-w_len*len(words):
        w_dic = {}
        for w in words: w_dic[w] = w_dic.get(w, 0) + 1
        j = i
        while w_dic and j <= len(s)-w_len:
            if s[j:j+w_len] in w_dic:
                w_dic[s[j:j+w_len]] -= 1
                if w_dic[s[j:j+w_len]] == 0:
                    del w_dic[s[j:j+w_len]]
                j += w_len
            else:
                break

        if not w_dic:
            rslt.append(i)

        i += 1

    return rslt

def test1():
    s = 'barfoothefoobarman'
    words = ['foo', 'bar']
    print(findSubstr(s, words))

def test2():
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(findSubstr(s, words))

def test3():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print(findSubstr(s, words))

def test4():
    s = "aaaaaaaa"
    words = ["aa","aa","aa"]
    print(findSubstr(s, words))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
