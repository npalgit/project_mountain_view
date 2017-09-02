#!/usr/bin/python
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y < 231.

Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       |   |

The above arrows point to positions where the corresponding bits are different.
#461
"""
def hDistance(x, y):
    s1 = bin(x)[2:]
    s2 = bin(y)[2:]
    i, j = len(s1)-1, len(s2)-1

    distance = 0

    while i >= 0 or j >= 0:
        ch1 = s1[i] if i >= 0 else '0'
        ch2 = s2[j] if j >= 0 else '0'
        if ch1 != ch2:
            distance += 1
        i -= 1
        j -= 1

    return distance

def test1():
    print(hDistance(1, 4))

if __name__ == '__main__':
    test1()
