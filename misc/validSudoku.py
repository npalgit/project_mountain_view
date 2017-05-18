#!/usr/bin/python
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#36
"""
def isValid(board):
    """
    Works and 89% performance. More concise solution available.
    """
    n_len = 9
    s = set()
    # check row
    for r in board:
        for n in r:
            if n is '.': continue
            if n in s: return False
            else: s.add(n)
        s.clear()

    # check column
    for i in range(n_len):
        for r in board:
            if r[i] is '.': continue
            if r[i] in s: return False
            else: s.add(r[i])
        s.clear()

    # check square
    sq_len = 3
    r_b = c_b = 0
    r_e = r_b+sq_len
    c_e = c_b+sq_len

    while r_b < n_len:
        while c_b < n_len:
            #print((r_b, r_e), (c_b, c_e))
            for i in range(r_b, r_e):
                for j in range(c_b, c_e):
                    if board[i][j] is '.': continue
                    if board[i][j] in s: return False
                    else: s.add(board[i][j])
            s.clear()
            c_b = c_e
            c_e += sq_len
        c_b = 0
        c_e = sq_len
        r_b = r_e
        r_e += sq_len

    return True

def isValid2(board):
    """
    Clear solution with more space. But beats 100%.
    """
    s = set()
    for i in range(0, 9):
        for j in range(0, 9):
            val = board[i][j]
            if val != '.':
                if (i, val) in s or (val, j) in s or (i/3, j/3, val) in s: return False
                s.add((i, val)) # different key, i is int, val is str
                s.add((val, j))
                s.add((i/3, j/3, val))

    return True

def test1():
    b = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print(isValid(b))

def test2():
    b = [".87654321","2........",".....7...","4........","5........","6........","7........","8........","9........"]
    print(isValid(b))

if __name__ == '__main__':
    test1()
    test2()
