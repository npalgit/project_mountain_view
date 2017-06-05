#!/usr/bin/python
"""
The demons had captured the princess (P) and imprisoned her in the
bottom-right corner of a dungeon. The dungeon consists of M x N rooms
laid out in a 2D grid. Our valiant knight (K) was initially positioned
in the top-left room and must fight his way through the dungeon to
rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses
health (negative integers) upon entering these rooms; other rooms
are either empty (0's) or contain magic orbs that increase the
knight's health (positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.

#174
"""
def rescue(dgn):
    w, h = len(dgn[0]), len(dgn)
    dp = [x[:] for x in [[0]*w]*h]
    dp[-1][-1] = max(-dgn[-1][-1], 0)
    for j in reversed(range(w-1)):
        dp[-1][j] = max(dp[-1][j+1]-dgn[-1][j], 0)
    for i in reversed(range(h-1)):
        dp[i][-1] = max(dp[i+1][-1]-dgn[i][-1], 0)

    for i in reversed(range(h-1)):
        for j in reversed(range(w-1)):
            dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dgn[i][j], 0)

    return dp[0][0]+1

def test1():
    dgn = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(rescue(dgn))

def test2():
    dgn = [[-3, 5]]
    print(rescue(dgn))

if __name__ == '__main__':
    test1()
    test2()
