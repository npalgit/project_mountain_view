#!/usr/bin/python
"""
Given a string, sort it in decreasing order based on the frequency of characters.
Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
#451
"""
class SortByFreq:
    def __init__(self):
        self.indices = range(128)
        self.freq = [0]*128

    def sortByFreq(self, s):
        # build freq array
        for char in s: self.freq[ord(char)] += 1
        self.indices.sort(cmp=self.cmp)
        res = ''
        for i in self.indices:
            if self.freq[i] == 0: break
            res += chr(i)*self.freq[i]

        return res

    def cmp(self, a, b):
        return self.freq[b] - self.freq[a]

def test1():
    s = 'tree'
    sol = SortByFreq()
    print(sol.sortByFreq(s))

def test2():
    s = 'Aabb'
    sol = SortByFreq()
    print(sol.sortByFreq(s))

if __name__ == '__main__':
    test1()
    test2()
