#!/usr/bin/python
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".iven two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
#67
REDDO: do it recursively
"""
def addB(b1, b2):
    if len(b2) < len(b1): b1, b2 = b2, b1
    max_len = len(b2)
    min_len = len(b1)
    len_diff = max_len - min_len
    co = 0
    b1, b2 = list(b1), list(b2)
    for i in reversed(range(max_len)):
        if i-len_diff >= 0:
            s = int(b1[i-len_diff]) + int(b2[i]) + co
        else:
            s = int(b2[i]) + co

        if s == 3:
            b2[i] = '1'
            co = 1
        elif s == 2:
            b2[i] = '0'
            co = 1
        elif s == 1:
            b2[i] = '1'
            co = 0
        elif s == 0:
            b2[i] = '0'
            co = 0
    if co:
        b2 = ['1'] + b2

    return ''.join(b2)

def addBinRecurs(b1, b2):
    if not b1: return b2
    if not b2: return b1
    if b1[-1] == '1' and b2[-1] == '1':
        return addBinRecurs(addBinRecurs(b1[:-1], b2[:-1]), '1')+ '0'
    if b1[-1] == '0' and b2[-1] == '0':
        return addBinRecurs(b1[:-1], b2[:-1])+'0'
    else:
        return addBinRecurs(b1[:-1], b2[:-1])+'1'

def addBinRecurs2(a, b):
    if a == '' and b == '':
        return ''
    if a == '':
        return addBinRecurs2('', b[:-1]) + b[-1]
    if b == '':
        return addBinRecurs2(a[:-1], '') + a[-1]

    if a[-1] == '1' and b[-1] == '1':
        return addBinRecurs2('1', addBinRecurs2(a[:-1], b[:-1])) + '0'
    if a[-1] == '0' and b[-1] == '0':
        return addBinRecurs2(a[:-1], b[:-1]) + '0'
    else:
        return addBinRecurs2(a[:-1], b[:-1]) + '1'

def test1():
    b1 = '1001'
    b2 = '11011'
    print(addB(b1, b2))
    print(addBinRecurs(b1, b2))
    print('--------------')

def test2():
    b1 = '1111'
    b2 = '1111'
    print(addB(b1, b2))
    print(addBinRecurs(b1, b2))

def test3():
    b1 = '11'
    b2 = '10001'
    print(addBinRecurs(b1, b2))
    print(addBinRecurs2(b1, b2))

if __name__ == '__main__':
    test1()
    test2()
    test3()
