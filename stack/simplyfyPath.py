#!/usr/bin/python
"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

#71
REDDO: maybe using stack is smart, did not think of it first try. Figured out the solution once knowing to use stack. simplier solution
"""

def simplifyPath(path):
    s = []

    while path:
        if path[0] == '/':
            path = path[1:]
            continue

        idx = path.find('/')

        if idx == -1:
            nxt = path
            idx = len(path)-1
        else:
            nxt = path[:idx]
        if s and nxt == '..':
            s.pop()
        elif nxt != '.' and nxt != '..':
            s.append(nxt)

        path = path[idx+1:]

    return '/'+'/'.join(s)

def simplifyPathSimple(path):
    places = [p for p in path.split('/') if p != '.' and p != '']
    stack = []
    for p in places:
        if p == '..':
            if stack: stack.pop()
        else:
            stack.append(p)

    return '/' + '/'.join(stack)

def test1():
    path = '/a/./b/../../c/'
    print(simplifyPath(path))

def test2():
    path = '/home/'
    print(simplifyPath(path))

def test3():
    path = '/../'
    print(simplifyPath(path))

def test4():
    path = '/home//foo/'
    print(simplifyPath(path))

def test5():
    path = '/...'
    print(simplifyPath(path))

def test6():
    path = '/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///'
    print(simplifyPath(path))

def test7():
    path = '///.///h///././/.///'
    print(simplifyPath(path))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
