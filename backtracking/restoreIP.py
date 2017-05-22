#!/usr/bin/python
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#93
"""
def restIP(s):
    """
    Got it on my own beats 51%.
    """
    res = []
    l = ''
    restIPHelper(s, 0, l, res, 0)
    return res

def restIPHelper(s, i, l, res, lvl):
    if (i == len(s) and lvl < 4) or lvl > 4: return
    if i == len(s) and lvl == 4:
        res.append(l)

    for e in range(i, i+3):
        if inRange(s, i, e):
            sec = s[i:e+1] if i == 0 else l+'.'+s[i:e+1]
            restIPHelper(s, e+1, sec, res, lvl+1)

def inRange(s, beg, end):
    if end >= len(s) or \
        int(s[beg:end+1]) > 255 or \
        (end != beg and s[beg] == '0'):
        return False

    return True

def test1():
    s = '25525511135'
    print(restIP(s))

def test2():
    s = '010011'
    print(restIP(s))

if __name__ == '__main__':
    test1()
    test2()
