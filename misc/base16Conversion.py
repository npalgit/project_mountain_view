#!/usr/bin/python
"""
Convert dec to hex.
based on #168
"""

def toHex(num):
    dict = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F':'6', 'G': '7', \
            'H': '8', 'I': '9', 'J': 'A', 'K': 'B', 'L': 'C', 'M': 'D', 'N': 'E', 'O': 'F'}
    
    rslt = convert(num)
    rslt = [dict[i] for i in rslt]
    return ''.join(rslt)

def convert(num):
    return "" if num == 0 else convert((num-1)/16) + chr((num-1)%16 + ord('A'))

def test1():
    print(toHex(1445))
    print(toHex(35559))

if __name__ == '__main__':
    test1()
