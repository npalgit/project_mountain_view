#!/usr/bin/python
"""
Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

For instance, to encrypt the word 'crime'

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

Explain your solution and analyze its time and space complexities.

Examples:

input:  word = "dnotq"
output: "crime"

input:  word = "flgxswdliefy"
output: "encyclopedia"
Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space. Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.

Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa. You may search the internet for the appropriate method.
"""
def encrypt(s):
    prev_step2 = 1
    res = ''
    for ch in s:
        val_ch = ord(ch)
        val_ch += prev_step2
        prev_step2 = val_ch
        while val_ch > ord('z'):
            val_ch -= 26
        res += chr(val_ch)
    return res

def decrypt(s):
    prev_step2 = 1
    res = ''
    for ch in s:
        val_ch = ord(ch)
        val_ch -= prev_step2
        while val_ch < ord('a'):
            val_ch += 26
        prev_step2 = val_ch + prev_step2
        res += chr(val_ch)
    return res

def test1():
    s = 'crime'
    print(s)
    encrypted_s = encrypt(s)
    print(encrypted_s)
    print(decrypt(encrypted_s))
    print('---------')

def test2():
    s = 'zebra'
    print(s)
    encrypted_s = encrypt(s)
    print(encrypted_s)
    print(decrypt(encrypted_s))
    print('---------')

if __name__ == '__main__':
    test1()
    test2()
