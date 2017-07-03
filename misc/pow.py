#!/usr/bin/python
"""
Implement pow(x, n). x is float, n is int

#50
REDDO: good to redo, to know how to implement with closed eyes.
"""
def pow(x, n):
    """
    default solution from lc
    """
    if n == 0:
        return 1

    if n < 0:
        n = -n
        x = 1/x

    return x*pow(x*x, n/2) if n%2 == 1 else pow(x*x, n/2)

def pow2(x, n):
    """
    self made solution.
    """
    if n == 0:
        return 1

    if n < 0:
        n = -n
        x = 1/x

    tmp = pow(x, n/2)
    if n%2 == 1:
        return x*tmp*tmp
    else:
        return tmp*tmp

def test1():
    x = 3
    n = 8
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test2():
    x = 3.3
    n = 7
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test3():
    x = 3
    n = 6
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test4():
    x = 3.0
    n = -8
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test5():
    x = 3.3
    n = -7
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test6():
    x = 3.0
    n = -6
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

def test7():
    x = 2.0
    n = -2147483648 
    print('pow({},{}):{}'.format(x, n, pow(x, n)))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
