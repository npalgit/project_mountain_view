#!/usr/bin/python
"""
Implement wildcard pattern matching with support for '?' and '*'.
#44
REDO: quick for practice. notice the special case invovles preprocessing.
"""
def wildCardMatching(s, p):
    dp = [x[:] for x in [[False]*(len(s)+1)]*(len(p)+1)]
    dp[-1][-1] = True

    for i in reversed(range(len(p))):
        if p[i] == '*':
            dp[i][-1] = True
        else:
            break

    for i in reversed(range(len(p))):
        for j in reversed(range(len(s))):
            if s[j] == p[i] or p[i] == '?':
                dp[i][j] = dp[i+1][j+1]
            elif p[i] == '*':
                # note dp[i+1][j+1] == True is optional
                if dp[i+1][j] == True or dp[i][j+1] == True or dp[i+1][j+1] == True:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    return dp[0][0]

def test1():
    s = 'abcde'
    p = 'a*c?e'
    print(wildCardMatching(s, p))

def test2():
    s = 'abcde'
    p = 'a*cfe'
    print(wildCardMatching(s, p))

def test3():
    s = ''
    p = 'a*cfe'
    print(wildCardMatching(s, p))

def test4():
    s = 'abcde'
    p = ''
    print(wildCardMatching(s, p))

def test5():
    s = 'abcde'
    p = '*'
    print(wildCardMatching(s, p))

def test6():
    s = 'a'
    p = 'a*'
    print(wildCardMatching(s, p))

def test7():
    s = ''
    p = '*'
    print(wildCardMatching(s, p))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
