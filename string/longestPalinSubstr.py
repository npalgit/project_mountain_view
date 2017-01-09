#!/usr/bin/python
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

        Input: "cbbd"

        Output: "bb"
leetcode #5
"""

def longestPalinSubstr_dp(str):
    """
    solution done using dynamic programming. Slower and uses more space than non-dp version.
    """
    l_str = len(str)

    if l_str == 0 or str is None:
        return ""

    rslt = [x[:] for x in [[0]*l_str]*l_str]
    extd = 0
    max_len = 1
    r_beg = 0

    j = 0
    while extd < l_str:
        for i in xrange(l_str):
            j = i+extd
            if j >= l_str:
                break
            if i == j:
                rslt[i][j] = True
            elif str[i] == str[j] and (j-i == 1 or rslt[i+1][j-1]):
                rslt[i][j] = True
                len_tmp = j-i+1
                if len_tmp > max_len:
                    max_len = len_tmp
                    r_beg = i
            else:
                rslt[i][j] = False
        extd += 1

    return str[r_beg:r_beg+max_len]

class LongestPalinSubstr:
    def __init__(self):
        self.p_diff = 0
        self.p_idx = 0

    def extendPalin(self, str, j, k):
        while j >= 0 and k < len(str) and str[j] == str[k]:
            tmp_diff = k-j+1

            if tmp_diff > self.p_diff:
                self.p_diff = tmp_diff
                self.p_idx = j

            j -= 1
            k += 1

    def longestPalinSubstr(self, str):
        # 1. look at i and i+1, if equal expand left and right
        # 2. if not equal, look at i, i+1, i+2, if palin, expand left and right
        # 3. if 1, then i += 1. if 2, then i += 2
        if str == None or len(str) < 2:
            return str

        for i in xrange(len(str)-1):
            # odd case 
            self.extendPalin(str, i, i)
            # even case
            self.extendPalin(str, i, i+1)

        return str[self.p_idx:self.p_idx+self.p_diff]

def test1():
    str = "babad"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test2():
    str = "cbbd"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test3():
    str = "kabbabbadefg"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test4():
    str = "k"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test5():
    str = "abcdefghi"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test6():
    str = "aaaa"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test7():
    str = ""
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

def test8():
    str = "kabbaabadefgabbaabba"
    print(longestPalinSubstr_dp(str))
    lps = LongestPalinSubstr()
    print(lps.longestPalinSubstr(str))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
