#!/usr/bin/python
"""
Count the number of prime numbers less than a non-negative number, n.
#204
"""
def countPrime(self, n):
    """
    TLE 17/20
    """
    if n == 0 or n == 1: return 0
    count = 0

    for val in range(2, n):
        if checkPrime(val):
            count += 1

    return count

def checkPrime(val):
    for i in range(2, val):
        if val % i == 0:
            return False
    return True

def test1():
    n = 2
    print(n, 'numPrime:{}'.format(countPrime(n)))
    n = 20
    print(n, 'numPrime:{}'.format(countPrime(n)))
    n = 30
    print(n, 'numPrime:{}'.format(countPrime(n)))
    n = 40
    print(n, 'numPrime:{}'.format(countPrime(n)))
    n = 100
    print(n, 'numPrime:{}'.format(countPrime(n)))

if __name__ == '__main__':
    test1()
