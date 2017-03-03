#!/usr/bin/python
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

leetcode #38
"""
def countSay(n):
    o_s = "11"
    if n == 1:
        return o_s

    for _ in xrange(1, n):
        n_s = ""
        count = 1
        i = 0
        while i < len(o_s)-1:
            if o_s[i] == o_s[i+1]:
                count += 1
            else:
                n_s += str(count)
                n_s += str(o_s[i])
                count = 1

            i += 1

        n_s += str(count)
        n_s += str(o_s[i])
        o_s = n_s

    return o_s

def test1():
    print(countSay(5))
    print("--------------")

def test2():
    print(countSay(6))
    print("-------------")

if __name__ == "__main__":
    test1()
    test2()

