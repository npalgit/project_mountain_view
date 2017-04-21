#!/usr/bin/python
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, Given s = "Hello World",
return 5.

#58
"""
def lenLast(s):
    l = 0
    i = len(s)-1

    while i>= 0 and s[i] == ' ':
        i -= 1

    while i >= 0 and s[i] != ' ':
        l += 1
        i -= 1

    return l

def test1():
    s = 'Hello World'
    print(lenLast(s))

def test2():
    s = 'a '
    print(lenLast(s))

def test3():
    s = ''
    print(lenLast(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
