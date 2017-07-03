#!/usr/bin/python
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty tank at one of the
gas stations.

Return the starting gas station's index if you can travel around the circuit once,
otherwise return -1.

#134
REDDO: need to find the pattern. I don't like this question that much. need to solve with no hints
"""

def calculategs(g, c):
    tnk = 0
    total = 0

    for i in range(len(g)):
        tmp = g[i] - c[i]

        tnk += tmp
        total += tmp

        if tnk < 0:
            tnk = 0
            start = i+1

    return start if total >=0 else -1

def test1():
    g = [1,2,3,4,5]
    c = [3,4,5,1,2]
    print(calculategs(g, c))

if __name__ == '__main__':
    test1()

