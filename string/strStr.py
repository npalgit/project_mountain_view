#!/usr/bin/python
"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
leetcode#28
"""
def strStr(haystack, needle):
    if not haystack or not needle:
        return -1

    for k, ktem in enumerate(haystack):
        i = k
        j = 0
        for j, jtem in enumerate(needle):
            if i == len(haystack):
                return -1

            if haystack[i] == jtem:
                i += 1
            else:
                break

        if j == len(needle)-1:
            return k

    return -1

def strStr_short(haystack, needle):
    for i in xrange(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

def test1():
    h = "aaaaababekl"
    n = "aaaba"
    print(strStr(h, n))
    print(strStr_short(h, n))
    print('-------------')

def test2():
    h = ""
    n = ""
    print(strStr(h, n))
    print(strStr_short(h, n))
    print('-------------')

def test3():
    h = ""
    n = "a"
    print(strStr(h, n))
    print(strStr_short(h, n))
    print('-------------')

def test4():
    h = "a"
    n = ""
    print(strStr(h, n))
    print(strStr_short(h, n))
    print('-------------')

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
