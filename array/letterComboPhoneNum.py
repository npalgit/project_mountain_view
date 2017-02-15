#!/usr/bin/python
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

leetcode #17
"""

def pairUp(s, ll, lvl, master_l):
    if lvl == len(ll):
        if s:
            master_l.append(s)
        return

    for c in ll[lvl]:
        pairUp(s+c, ll, lvl+1, master_l)

def letterComboPN(digit_str):
    mp = { \
        '2':'abc', \
        '3':'def', \
        '4': 'ghi', \
        '5': 'jkl', \
        '6': 'mno', \
        '7': 'pqrs', \
        '8': 'tuv', \
        '9': 'wxyz' \
    }

    master_l = []
    ll = []

    for n in digit_str:
        ll.append(mp[n])
    print(ll)

    pairUp('', ll, 0, master_l)

    return master_l

def test1():
    print(letterComboPN('23'))

def test2():
    print(letterComboPN('234'))

def test3():
    print(letterComboPN('54'))

def test4():
    print(letterComboPN(''))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
