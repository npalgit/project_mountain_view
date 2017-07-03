#!/usr/bin/python
"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

No leading, trailing, or multiple spaces in between words.

#151
REDDO: part where clean space happens
"""
def reverseWinStr(s):
    l = list(s)
    reverse(l, 0, len(l)-1)
    beg = 0
    for idx in range(len(l)+1):
        if idx == len(l) or l[idx] == ' ':
            reverse(l, beg, idx-1)
            beg = idx+1

    return ''.join(clean(l))

def reverse(l, beg, end):
    while beg < end:
        l[beg], l[end] = l[end], l[beg]
        beg += 1
        end -= 1

def clean(l):
    n = len(l)
    i, j = 0, 0
    while j < n:
        while j < n and l[j] == ' ': j += 1
        while j < n and l[j] != ' ':
            l[i] = l[j]
            i += 1
            j += 1
        while j < n and l[j] == ' ': j += 1

        if j < n:
            l[i] = ' '
            i += 1
    return l[:i]

def test1():
    s = 'abc   defg hijkl   '
    print(reverseWinStr(s))

if __name__ == '__main__':
    test1()
