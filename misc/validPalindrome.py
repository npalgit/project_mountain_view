#!/usr/bin/python
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
#125
"""
def validPalin(s):
    rslt = []
    for i in s:
        h = ord(i)
        if h <= 0x5a and h >= 0x41 or h >= 0x61 and h <= 0x7a or h >= 0x30 and h <= 0x39:
            rslt.append(i.lower())

    beg, end = 0, len(rslt)-1
    while beg <= end:
        if rslt[beg] != rslt[end]: return False
        beg += 1
        end -= 1

    return True

def test1():
    s = "A man, a plan, a canal: Panama"
    print(validPalin(s))

if __name__ == '__main__':
    test1()
