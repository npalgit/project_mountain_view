#!/usr/bin/python
"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
#322
"""
from collections import deque

def cc(t, cs):
    """
    BFS solution. 78% -> 88%. First attempt did not include visited[].
    List of visited reduces repeated calls.
    space: O(t): the deque size max out at t.
    time: O(n*t): n, iterate through each c itm. q max len is t. Can't be more than t
    """
    q = deque()
    q.append((t, 0))
    visited = [False]*(t+1)
    visited[t] = True

    while q:
        n = q.popleft()
        if n[0] == 0:
            return n[1]

        for c in cs:
            val = n[0]-c
            if val == 0:
                return n[1]+1
            elif val > 0 and not visited[val]:
                new_n = (val, n[1]+1)
                q.append(new_n)
                visited[val] = True

    return -1

def cc_dp(t, cs):
    """
    50%. Even the discussion solution is around this peformance.
    """
    rslt = [0]*(t+1)

    for i in range(1, t+1):
        vs = [rslt[i-x] for x in cs if i >= x and rslt[i-x]>-1]
        if not vs:
            rslt[i] = -1
        else:
            rslt[i] = min(vs)+1
    return rslt[-1]

def test1():
    t = 11
    cs = [1, 2, 5]
    print(cc(t, cs))
    print(cc_dp(t, cs))
    print('-------------')

def test2():
    t = 3
    cs = [2]
    print(cc(t, cs))
    print(cc_dp(t, cs))
    print('-------------')

def test3():
    t = 10
    cs = [5, 2, 1, 10]
    print(cc(t, cs))
    print(cc_dp(t, cs))
    print('-------------')

def test4():
    t = 4
    cs = [2]
    print(cc(t, cs))
    print(cc_dp(t, cs))
    print('-------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
