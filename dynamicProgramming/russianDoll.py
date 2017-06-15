!/usr/bin/python
"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], 
y6the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#354
"""
def russianDoll(envs):
    if not envs: return 0
    envs.sort(cmp=cmp)
    dp = [0]*len(envs)
    dp[0] = envs[0][1]
    l_env = [el[1] for el in envs[1:]]
    max_len = 1

    for x in l_env:
        if x > dp[max_len-1]:
            dp[max_len] = x
            max_len += 1
        else:
            idx = binSearch(l_env, 0, max_len, x)
            dp[idx] = x

    return max_len

def cmp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    return a[0] - b[0]

def binSearch(nums, beg, end, k):
    while beg < end:
        mid = beg + (end-beg)/2
        if k <= nums[mid]:
            end = mid
        else:
            beg = mid+1
    return beg

def test1():
    nums = [[5,4],[6,4],[6,7],[2,3]]
    print(russianDoll(nums))

if __name__ == '__main__':
    test1()
