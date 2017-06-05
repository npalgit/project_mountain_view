#!/usr/bin/python
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

#165
"""
def compareVersions(v1, v2):
    s_v1 = v1.split('.')
    s_v2 = v2.split('.')
    i = 0

    len_v1, len_v2 = len(s_v1), len(s_v2)
    len_s = max(len_v1, len_v2)

    for i in range(len_s):
        n1 = int(s_v1[i]) if i < len_v1 else 0
        n2 = int(s_v2[i]) if i < len_v2 else 0

        if n1 < n2: return -1
        elif n1 > n2: return +1

    return 0

def test1():
    v2 = '1.23.3.1'
    v1 = '1.23.3'
    print(compareVersions(v1, v2))

def test2():
    v2 = '01'
    v1 = '1'

    print(compareVersions(v1, v2))

if __name__ == '__main__':
    test1()
    test2()
