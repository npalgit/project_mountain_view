#!/usr/bin/python
"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a characte

#72
REDDO
"""
def editDistance(w1, w2):
    dp = [x[:] for x in [[0]*(len(w1)+1)]*(len(w2)+1)]

    for i in range(len(w2)+1):
        dp[len(w2)-i][-1] = i

    for j in range(len(w1)+1):
        dp[-1][len(w1)-j] = j

    for i in reversed(range(len(w2))):
        for j in reversed(range(len(w1))):
            if w1[j] == w2[i]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])+1

    return dp[0][0]

def ed_dfs_r(w1, w2):
    """
    TLE 24/1146
    """
    if not w1 or not w2: return len(w1) if not w2 else len(w2)

    if w1[0] == w2[0]: return ed_dfs_r(w1[1:], w2[1:])

    return min(ed_dfs_r(w1, w2[1:]), ed_dfs_r(w1[1:], w2), ed_dfs_r(w1[1:], w2[1:]))+1
def test1():
    w1 = 'execution'
    w2 = 'intention'
    print(editDistance(w1, w2))

if __name__ == '__main__':
    test1()
