#!/usr/bin/python
"""
generate gray code sequence
#89
Stupid question only involes pattern finding.
"""
def gc(n):
    return [i ^ (i/2) for i in range(pow(2, n))]

def test1():
   print(gc(2))

if __name__ == '__main__':
    test1()
