#!/usr/bin/python
"""
LinkedIn hacker rank challenge.
Given a list of movie ratings, can contain positive or negative.
Select movies in such a way to maximize the total rating when you can
skip at most 1 movie.

e.g.
ratings = [9, -1, -3, 4, 5]
ans = 17, picked [9, -1, 4, 5]

rating = [-1, -2, -3, -4, -5]
ans = -6, picked [-2, -4]

rating = [-20]
ans = 0, don't pick any movie
"""
def maxRatings(ratings):
    if not ratings: return 0
    if len(ratings) < 2:
        return max(0, ratings[0])

    dp = [0]*(len(ratings))
    dp[0] = ratings[0]
    dp[1] = max(ratings[1], ratings[0]+ratings[1])

    for i in range(2, len(ratings)):
        dp[i] = max(dp[i-1], dp[i-2])+ratings[i]

    return max(dp[-1],dp[-2])

def test1():
    ratings = [9, -1, -3, 4, 5]
    print(maxRatings(ratings))

def test2():
    ratings = [-1, -2, -3, -4, -5]
    print(maxRatings(ratings))

def test3():
    ratings = [-20]
    print(maxRatings(ratings))

if __name__ == '__main__':
    test1()
    test2()
    test3()
