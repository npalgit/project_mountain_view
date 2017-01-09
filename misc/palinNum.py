#!/usr/bin/python
"""
Palindrome Number   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 174888
Total Submissions: 512928
Determine whether an integer is a palindrome. Do this without extra space.

#leetcode #9
REDO
"""
def isPalindrome(x):
    if x < 0 or (x != 0 and x%10 == 0):
        return False
    rev = 0
    while (x > rev):
        rev = rev*10 + x%10
        x /= 10
    return rev == x or rev/10 == x

def test1():
    x = 1234321
    print(isPalindrome(x))

def test2():
    x = 302140412
    print(isPalindrome(x))

def test3():
    x = 123321
    print(isPalindrome(x))

def test4():
    x = 0
    print(isPalindrome(x))

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
