#!/usr/bin/python
"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
#190 
REDO: good question
"""
def reverseBits(n):
    res = 0
    for _ in range(31):
        res += n & 1
        n >>= 1
        res <<= 1

    return res + n

def reverseInt(n):
    res = 0
    cache = {}

    for _ in range(3):
        res += reverseByte(n&0xff, cache)
        res <<= 8
        n >>= 8
    return res + reverseByte(n&0xff, cache)

def reverseByte(b, cache):
    o_b = b
    res = cache.get(b)
    if res:
        return res
    res = 0
    for i in range(7):
        res += b & 1
        b >>= 1
        res <<= 1
    res += b
    cache[o_b] = res
    return res


def test1():
    n = 0b01011011101111
    print(bin(reverseBits(n)))
    print(bin(reverseInt(n)))

def test2():
    n = 0x7f127f12
    print(bin(reverseBits(n)))
    print(bin(reverseInt(n)))

if __name__ == '__main__':
    test1()
    test2()
