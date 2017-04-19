#!/usr/bin/python
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.

#37
REDO: good quesiton to get re-acquinted with. did not struggle too much.
"""

def solver(board):
    """
    Original solution based on ValidSudoku, but time limit exceeded.
    """
    b = map(list, board)
    dfs(b)
    return [''.join(r) for r in b]

def findEmpty(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == '.': return i, j
    return -1, -1

def dfs(b):
    i, j = findEmpty(b)
    if i == -1 and j == -1:
        return True

    for n in map(str, [x for x in range(1, 10)]):
        b[i][j] = n
        if isValid(b) and dfs(b):
            return True
        b[i][j] = '.'

    return False

def isValid(b):
    s = set()
    for i in range(0, 9):
        for j in range(0, 9):
            val = b[i][j]
            if val != '.':
                if (i, val) in s or (val, j) in s or (i/3, j/3, val) in s: return False
                s.add((i, val)) # different key, i is int, val is str
                s.add((val, j))
                s.add((i/3, j/3, val))

    return True

def solverFast(board):
    """
    Sol 2, around 20% fasted so far
    """
    b = map(list, board)
    dfsFast(b)
    return [''.join(r) for r in b]

def dfsFast(b):
    i, j = findEmpty(b)
    if i == -1 and j == -1:
        return True
    for c in map(str, [x for x in range(1, 10)]):
        if isValidShort(b, i, j, c):
            b[i][j] = c
            if dfsFast(b): return True
            b[i][j] = '.'

    return False

def solverFastNestedLoop(board):
    """
    Sol 3, the nested loop in dfsFastNestedLoop, make lc compiler time out.
    """
    b = map(list, board)
    dfsFast(b)
    return [''.join(r) for r in b]

def dfsFastNestedLoop(b):
    for i in range(9):
           for j in range(9):
               if b[i][j] != '.': continue
    for c in map(str, [x for x in range(1, 10)]):
        if isValidShort(b, i, j, c):
            b[i][j] = c
            if dfsFast(b): return True
            b[i][j] = '.'

    return False

def isValidShort(b, i, j, c):
    """
    Really smart solution
    """
    for idx in range(9):
        if b[i][idx] == c: return False
        if b[idx][j] == c: return False
        if b[3*(i/3)+idx/3][3*(j/3)+idx%3] == c: return False

    return True

def test1():
    b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print(solverFast(b))
    b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print(solverFastNestedLoop(b))

if __name__ == '__main__':
    test1()
