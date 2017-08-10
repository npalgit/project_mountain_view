#!/usr/bin/python
"""
Essentially catalan number.
"""
def numPath_dp(n):
    dp = [x[:] for x in [[0]*(n+1)]*(n+1)]
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if j == n-1 and i == n-1:
                dp[i][j] = 1
            elif i <= j:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]

def numPath_mem(n):
    mem = {}
    mem[(n-1, n-1)] = 1
    ans = dfs(0, 0, n, mem)
    return ans

def dfs(i, j, n, mem):

    if (i, j) in mem:
        return mem[(i, j)]
    elif j < i:
        return 0
    else:
        down = dfs(i+1, j, n, mem) if i < n else 0
        right = dfs(i, j+1, n, mem) if j < n else 0
        res = right + down
        mem[(i, j)] = res
        return res

def test1():
    print(numPath_dp(4))
    print(numPath_mem(4))
    print(numPath_dp(5))
    print(numPath_mem(5))
    print(numPath_dp(6))
    print(numPath_mem(6))

if __name__ == '__main__':
    test1()

