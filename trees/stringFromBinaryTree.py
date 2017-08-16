#!/usr/bin/python
"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
#606
"""
from btNode import BTNode

def constructStr(n):
    if not n: return ''
    res = ''
    lhs, rhs = '', ''

    lhs = constructStr(n.left)
    rhs = constructStr(n.right)
    tail = ''
    if not lhs and not rhs:
        tail = ''
    elif lhs and not rhs:
        tail = '({})'.format(lhs)
    else:
        tail = '({})({})'.format(lhs, rhs)

    return str(n.val) + tail

def constructStr2_top(n):
    if not n: return ""
    s = constructStr2(n)
    return s[1:-1]

def constructStr2(n):
    if not n: return None
    lhs = constructStr2(n.left)
    rhs = constructStr2(n.right)

    if not lhs and not rhs:
        tail = ''
    elif not rhs:
        tail = lhs
    else:
        if not lhs: lhs = '()'
        tail = lhs + rhs
    return '(' + str(n.val) + tail + ')'

def test1():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)

    n1.left = n2
    n1.right = n3
    n2.left = n4

    print(constructStr(n1))
    print(constructStr2_top(n1))

def test2():
    n1 = BTNode(1)
    n2 = BTNode(2)
    n3 = BTNode(3)
    n4 = BTNode(4)

    n1.left = n2
    n2.right = n4
    n1.right = n3
    print(constructStr(n1))
    print(constructStr2_top(n1))


if __name__ == '__main__':
    test1()
    test2()
