#!/usr/bin/python
"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
#60
REDO: smart algorithm and index manipulation
"""
from math import factorial
def permSeq(n, k):
    k = k-1
    facs = [factorial(i) for i in range(n)]
    l = [i for i in range(1, n+1)]
    rslt = ''
    for i in range(1, n):
        idx = k/facs[n-i]
        k = k%facs[n-i] # alt: k = k-idx*facs[n-i]
        rslt += str(l[idx])
        del l[idx]

    rslt += str(l[0])
    return rslt

def test1():
    print(permSeq(4, 14))

if __name__ == '__main__':
    test1()
