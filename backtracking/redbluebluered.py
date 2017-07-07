#!/usr/bin/python
"""
Dropbox hackerrank challenge
given pattern, and input
pattern has single characters
input can contain many words.
see if pattern and input match each other

test1():
    pattern = 'abba'
    input = 'redbluebluered'
    out => True

test2():
    pattern = 'aaaa'
    input = 'redbluebluered'
    out => False

test3():
    pattern = 'abcdeeee'
    input = 'onetwothreefourcowcowcowcow'
    out => True

test4():
    pattern = 'abcdb'
    input = 'tobeornottobe'
    out => True

test5():
    pattern = 'abba'
    input = 'redredredred'
    out => False
"""
def wpattern(pattern, input):
    dic = {}
    return dfs(pattern, input, dic)

def dfs(pattern, input, dic):
    if not input and not pattern: return True
    if not input or not pattern: return False
    char = pattern[0]
    if char in dic:
        if input.startswith(dic[char]):
            return dfs(pattern[1:], input[len(dic[char]):], dic)
        else:
            return False
    else:
        for i in range(1, len(input)+1):
            if input[:i] in dic.values():
                continue
            dic[char] = input[:i]
            if dfs(pattern[1:], input[i:], dic):
                return True
            del dic[char]

    return False

def test1():
    pattern = 'abba'
    input = 'redbluebluered'
    print(wpattern(pattern, input))

def test2():
    pattern = 'aaaa'
    input = 'redbluebluered'
    print(wpattern(pattern, input))

def test3():
    pattern = 'abcdeeee'
    input = 'onetwothreefourcowcowcowcow'
    print(wpattern(pattern, input))

def test4():
    pattern = 'abcdb'
    input = 'tobeornottobe'
    print(wpattern(pattern, input))

def test5():
    pattern = 'abba'
    input = 'redredredred'
    print(wpattern(pattern, input))

def test6():
    pattern = 'cdf'
    input = 'blueredblue'
    print(wpattern(pattern, input))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
