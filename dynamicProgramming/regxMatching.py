#!/usr/bin/python
"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

leetcode #10
REDO- dp is a little bit complicated with details, this is really a difficult one
"""

def isRegxMatchingBrute(s, p):
    if not p:
        return s is ''

    if len(p) > 1 and p[1] == '*':
        return isRegxMatchingBrute(s, p[2:]) or \
                (s is not '' and (s[0] == p[0] or p[0] == '.') and isRegxMatchingBrute(s[1:], p))
    else:
        return s is not '' and (s[0] == p[0] or p[0] == '.') and isRegxMatchingBrute(s[1:], p[1:])

def isRegxMatchingDp(s, p):
    w = len(s)
    h = len(p)

    rslt = [x[:] for x in [[False]*(w+1)]*(h+1)]

    rslt[h][w] = True
    for i in reversed(xrange(h)):
        if i < h-1 and p[i+1] == '*' and rslt[i+2][w]:
            rslt[i][w] = True

    for p_i in reversed(xrange(h)):
        for s_i in reversed(xrange(w)):
            if p_i < h-1 and p[p_i+1] == '*':
                rslt[p_i][s_i] = rslt[p_i+2][s_i] or \
                                ((p[p_i] == s[s_i] or p[p_i] == '.') and rslt[p_i][s_i+1])
            else:
                rslt[p_i][s_i] = rslt[p_i+1][s_i+1] and (p[p_i] == s[s_i] or p[p_i] == '.')

    print_mtx(rslt)

    return rslt[0][0]

def print_mtx(mtx):
    for x in mtx:
        print(map(int, x))

def test1():
    s = "aa"
    p = "a"
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test2():
    s = 'aa'
    p = 'aa'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test3():
    s = 'aaa'
    p = 'aa'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test4():
    s = "aa"
    p = "a*"
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test5():
    s = 'ab'
    p = '.*'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test6():
    s = 'aab'
    p = 'c*a*b'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test7():
    s = 'aaa'
    p = 'aaaa'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s, p))
    print('------------')

def test8():
    s = 'dddegi'
    p = '.*d*de.i'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s, p))
    print('------------')

def test9():
    s = "aa"
    p = "aa*"
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test10():
    s = 'ab'
    p = '.*b'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test11():
    s = 'ab'
    p = '.*c'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test12():
    s = 'abbcdefg'
    p = '.*.*.*.*.*.*.*.*'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')

def test13():
    s = ''
    p = 'c*c*'
    print('s:{}, p:{}'.format(s, p))
    print(isRegxMatchingBrute(s, p))
    print(isRegxMatchingDp(s,p))
    print('------------')


if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    #test6()
    #test7()
    #test8()
    #test9()
    #test10()
    #test11()
    #test12()
    test13()
