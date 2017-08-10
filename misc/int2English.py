#!/usr/bin/python
"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#273
"""
def int2Words(n):
    res = words(n)
    return ' '.join(res) if res else 'Zero'

def words(n):
    if not n: return []
    to19  = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()

    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    if n < 20:
        return [to19[n-1]]
    if n < 100:
        return [tens[n/10-2]] + words(n%10)
    if n < 1000:
        return [to19[n/100-1]] + ['Hundred'] + words(n%100)

    res = words(n%1000)
    n /= 1000
    for k in ['Thousand', 'Million', 'Billion']:
        if not n: break
        curr = words(n%1000)
        if curr:
            res = curr + [k] + res
        else:
            res = curr + res
        n /= 1000

    return res

def test1():
    print(int2Words(1050001))
    print(int2Words(0))

if __name__ == '__main__':
    test1()
