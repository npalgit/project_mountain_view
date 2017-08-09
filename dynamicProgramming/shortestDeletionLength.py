#!/usr/bin/python
"""
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
question from pramp
"""
def deletion_distance(str1, str2):
    len_n = len(str1) # col
    len_m = len(str2) # row
    # declare a matrix
    dp = [x[:] for x in [[0]*(len_n+1)]*(len_m+1)]

    # preprocess fill last elements in row and column
    # fill last row
    for idx, j in enumerate(reversed(range(len_n)), 1):
      dp[-1][j] = idx

    # fill last col
    for idx, i in enumerate(reversed(range(len_m)), 1):
      dp[i][-1] = idx

    # normal go through
    for i in reversed(range(len_m)):
        for j in reversed(range(len_n)):
            if str2[i] == str1[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])+1

    return dp[0][0]

def test1():
    str1 = 'dog'
    str2 = 'frog'
    print(deletion_distance(str1, str2))

def test2():
    str1 = 'some'
    str2 = 'some'
    print(deletion_distance(str1, str2))

def test3():
    str1 = 'some'
    str2 = 'thing'
    print(deletion_distance(str1, str2))

def test4():
    str1 = ''
    str2 = 'abcdef'
    print(deletion_distance(str1, str2))

def test4():
    str1 = 'e'
    str2 = 'abcdef'
    print(deletion_distance(str1, str2))

def test5():
    str1 = ''
    str2 = ''
    print(deletion_distance(str1, str2))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
