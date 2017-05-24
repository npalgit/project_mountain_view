#!/usr/bin/python
"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
#65
"""
def validN(s):
    states = [{'blank': 0, 'sign': 1, 'digit':2, '.':3}, \
              {'digit': 2, '.': 3}, \
              {'digit': 2, '.': 4, 'e': 5, 'blank': 8}, \
              {'digit': 4}, \
              {'digit': 4, 'e': 5, 'blank':8}, \
              {'digit': 6, 'sign': 7}, \
              {'digit': 6, 'blank': 8}, \
              {'digit': 6}, \
              {'blank': 8}]

    curr_state = 0
    for c in s:
        if c in '0123456789':
            c = 'digit'
        if c == '+' or c == '-':
            c = 'sign'
        if c == ' ':
            c = 'blank'
        if c not in states[curr_state].keys():
            return False
        curr_state = states[curr_state][c]
    if curr_state not in [2, 4, 6, 8]:
        return False

    return True

def test1():
    print(validN('0'))
    print(validN(' 0.1 '))
    print(validN('abc'))
    print(validN('1 a'))
    print(validN('2e10'))
    print(validN('-1.'))

if __name__ == '__main__':
    test1()
