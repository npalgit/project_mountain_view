#!/usr/bin/python
"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
#536
"""
'''
4(2(3)(1))(6(5))

s[0] -> n, split by braces
n.left = (2(3)(1)) -> 2(3)(1)
n.right = (6(5)) ->  6(5)
how do you find the one in the middle and split?
'''

def constructTree(s):
    if not s: return None
    n = BTNode(s[0])
    lhs_s, rhs_s = split_str(s[1:])
    lhs = constructTree(lhs_s)
    rhs = constructTree(rhs_s)
    return n

def split_str(s):
    if not s: return "", ""
    s = s[1:-1]
    num_left = 0
    break_idx = 0
    for idx, itm in enumerate(s):
        if itm == '(':
            num_left += 1
        elif itm == ')':
            num_left -= 1
        if num_left < 0:
            break_idx = idx
            break
    return s[:break_idx], s[break_idx+2:]

def test1():
    pass

if __name__ == '__main__':
    test1()
