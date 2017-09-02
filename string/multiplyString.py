#!/usr/bin/python
"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

leetcode#43
"""

def mulStrings(l1, l2):
    """
    This solution keeps int then convert to string at the end.
    """
    rslt = 0
    for n1 in l1:
        t = 0
        for n2 in l2:
            t *= 10
            t += (ord(n1)-0x30)*(ord(n2)-0x30)

        rslt *= 10
        rslt += t

    return str(rslt)

def mulStringsLC_LittleEndian(l1, l2):
    """
    Interesting solution. Little Endian
    """
    rslt = [0]*(len(l1)+len(l2))
    for j, n2 in enumerate(reversed(l2)):
        for i, n1 in enumerate(reversed(l1)):
            rslt[i+j] += (ord(n1)-0x30)*(ord(n2)-0x30)
            rslt[i+j+1] += rslt[i+j]/10
            rslt[i+j] = rslt[i+j]%10

    while len(rslt) > 1 and rslt[-1] == 0: rslt.pop()

    return ''.join(map(str, rslt[::-1]))

def mulStringsLC_BigEndian(l1, l2):
    """
    Interesting solution. Big Endian
    """
    rslt = [0]*(len(l1)+len(l2))
    for j, n2 in reversed(list(enumerate(l2))):
        for i, n1 in reversed(list(enumerate(l1))):
            rslt[i+j+1] += (ord(n1)-0x30)*(ord(n2)-0x30)
            rslt[i+j] += rslt[i+j+1]/10
            rslt[i+j+1] = rslt[i+j+1]%10
    while len(rslt) > 1 and rslt[0] == 0: rslt.pop(0)

    return ''.join(map(str, rslt))

def mulStr_r(s1,  s2):
    res = [0]*(len(s1)+len(s2))
    for i in range(len(s1)):
        for j in range(len(s2)):
            ch_1 = s1[len(s1)-i-1]
            ch_2 = s2[len(s2)-j-1]
            res[i+j] += (ord(ch_1)-ord('0'))*(ord(ch_2)-ord('0'))
            res[i+j+1] += res[i+j]/10
            res[i+j] = res[i+j]%10

    while res and res[-1] == 0: res.pop()
    return ''.join(map(str, res[::-1]))

def test1():
    l1 = "1234"
    l2 = "6701"
    print(mulStrings(l1, l2))
    print(mulStringsLC_LittleEndian(l1, l2))
    print(mulStringsLC_BigEndian(l1, l2))
    print(mulStr_r(l1, l2))
    print("----------------")

def test2():
    l1 = "98765"
    l2 = "0"
    print(mulStrings(l1, l2))
    print(mulStringsLC_LittleEndian(l1, l2))
    print(mulStringsLC_BigEndian(l1, l2))
    print(mulStr_r(l1, l2))
    print("----------------")

def test3():
    l1 = "12"
    l2 = "545"
    print(mulStrings(l1, l2))
    print(mulStringsLC_LittleEndian(l1, l2))
    print(mulStringsLC_BigEndian(l1, l2))
    print(mulStr_r(l1, l2))
    print("----------------")

def test4():
    l1 = "4"
    l2 = "7"
    print(mulStrings(l1, l2))
    print(mulStringsLC_LittleEndian(l1, l2))
    print(mulStringsLC_BigEndian(l1, l2))
    print(mulStr_r(l1, l2))
    print("----------------")

def test5():
    l1 = "99"
    l2 = "9"
    print(mulStrings(l1, l2))
    print(mulStringsLC_LittleEndian(l1, l2))
    print(mulStringsLC_BigEndian(l1, l2))
    print(mulStr_r(l1, l2))
    print("----------------")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
