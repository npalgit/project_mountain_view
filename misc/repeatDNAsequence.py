#!/usr/bin/python
"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#187
"""
def repeatSeq(s):
    """
    first try 93.05% submission
    """
    seen, repeated = set(), set()
    for i in range(0, len(s)-9):
        seq = s[i:i+10]
        if seq not in seen: seen.add(seq)
        else: repeated.add(seq)
    return [i for i in repeated]

def repeatSeqLessMem(s):
    if len(s) < 11: return []
    seen, repeated = set(), set()
    dic = {'A':0, 'C':1, 'G':2, 'T':3}
    rslt = []

    # 0011 1111 1111 1111
    mask = 0x0003ffff
    code = 0
    for i in range(9):
        #code = (code & mask) << 2 | dic[s[i]]
        code <<= 2
        code |= dic[s[i]]

    for i in range(9, len(s)):
        code = ((code & mask) << 2) | dic[s[i]]
        if code not in seen:
            seen.add(code)
        elif code in seen and code not in repeated:
            repeated.add(code)
            rslt.append(s[i-9: i+1])

    return rslt

def test1():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(repeatSeq(s))
    print(repeatSeqLessMem(s))

if __name__ == '__main__':
    test1()
