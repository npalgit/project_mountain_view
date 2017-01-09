#!/usr/bin/python
def atoi(s):
    if s == None or s == '':
        return 0
    sign = 1
    i = 0
    while s[i] == ' ':
        i += 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    elif ord(s[i]) < 0x30 or ord(s[i]) > 0x39:
        return 0
    rslt = 0
    while i < len(s) and ord(s[i]) >= 0x30 and ord(s[i]) <= 0x39:
        rslt *= 10
        rslt += ord(s[i]) - 0x30
        i += 1

    rslt *= sign
    if rslt < -2147483648:
        return -2147483648
    if rslt > 2147483647:
        return 2147483647

    return rslt

def test1():
    s = "-1234"
    print(atoi(s))

def test2():
    s = "+1234abc"
    print(atoi(s))

def test3():
    s = "      +532"
    print(atoi(s))

def test4():
    s = "        ab123"
    print(atoi(s))

def test5():
    s = "a          - 231"
    print(atoi(s))

def test6():
    s = "4232-12"
    print(atoi(s))

def test7():
    s = ""
    print(atoi(s))

def test8():
    s = "2147483648"
    print(atoi(s))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
