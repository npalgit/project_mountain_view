#!/usr/bin/python
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'
A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
#130
"""
from collections import deque

def flipSorroundedOXB(b):
    """
    83.4% to 71.3% performance
    """
    if b == [] or b == [[]]: return

    h = len(b)
    w = len(b[0])

    # process border first
    for j in range(w):
        boundCond((0, j), b)
        boundCond((h-1, j), b)

    # process border first
    for i in range(h):
        boundCond((i, 0), b)
        boundCond((i, w-1), b)

    # flip O to X
    for i in range(1, h-1):
        for j in range(1, w-1):
            if b[i][j] == 'O': b[i][j] = 'X'

    # flip B to O
    for i in range(h):
        for j in range(w):
            if b[i][j] == 'B': b[i][j] = 'O'

    return b

def boundCond(n, b):
    i, j = n[0], n[1]
    if b[i][j] != 'O': return
    q = deque()
    b[i][j] = 'B'
    q.append(n)

    while q:
        n = q.popleft()
        i, j = n[0], n[1]
        for nbr in getNbrsOXB(n, b):
            b[nbr[0]][nbr[1]] = 'B'
            q.append(nbr)

def getNbrsOXB(n, b):
    h = len(b)
    w = len(b[0])
    nbrs = []
    i, j = n[0], n[1]

    if i-1 >= 0 and b[i-1][j] == 'O': nbrs.append((i-1, j))
    if i+1 < h and b[i+1][j] == 'O': nbrs.append((i+1, j))
    if j-1 >= 0 and b[i][j-1] == 'O': nbrs.append((i, j-1))
    if j+1 < w and b[i][j+1] == 'O': nbrs.append((i, j+1))

    return nbrs

def flipSorrounded(b):
    """
    Accepted 26.72% - 11.91% acceptance
    """
    h = len(b)
    w = len(b[0])

    visited = [x[:] for x in [[0]*w]*h]
    flip = True
    q = deque()
    for i in range(h):
        for j in range(w):
            if visited[i][j]: continue
            if b[i][j] == 'O':
                visited[i][j] = True
                q.append((i, j))
            flip_itms = []

            while q:
                n = q.popleft()
                if isBorder(n, w, h): flip = False
                if flip: flip_itms.append(n)
                for nbr in getNbrs(n, b, visited):
                    visited[nbr[0]][nbr[1]] = True
                    q.append(nbr)

            if flip: flip_area(b, flip_itms)
            flip = True

    return b

def getNbrs(n, b, visited):
    h = len(b)
    w = len(b[0])
    nbrs = []
    i, j = n[0], n[1]

    if i-1 >= 0 and not visited[i-1][j] and b[i-1][j] == 'O': nbrs.append((i-1, j))
    if i+1 < h and not visited[i+1][j] and b[i+1][j] == 'O': nbrs.append((i+1, j))
    if j-1 >= 0 and not visited[i][j-1] and b[i][j-1] == 'O': nbrs.append((i, j-1))
    if j+1 < w and not visited[i][j+1] and b[i][j+1] == 'O': nbrs.append((i, j+1))

    return nbrs

def isBorder(n, w, h):
    i, j = n[0], n[1]
    if i-1 < 0 or j-1 < 0 or i+1 >= h or j+1 >= w:
        return True

    return False

def flip_area(b, flip_itms):
    for itm in flip_itms:
        b[itm[0]][itm[1]] = 'X'

def test1():
    b = [\
    ['X','X','X','X'], \
    ['X','O','O','X'], \
    ['X','X','O','X'], \
    ['X','O','X','X']]

    flipSorrounded(b)

    for l in b:
        print(l)

    b = [\
    ['X','X','X','X'], \
    ['X','O','O','X'], \
    ['X','X','O','X'], \
    ['X','O','X','X']]

    flipSorroundedOXB(b)

    for l in b:
        print(l)
    print('-------------')

def test2():
    b = [['O', 'X']]
    flipSorrounded(b)

    for l in b:
        print(l)

    b = [['O', 'X']]
    flipSorroundedOXB(b)

    for l in b:
        print(l)
    print('-------------')

def test3():
    b = [[]]
    flipSorrounded(b)

    for l in b:
        print(l)

    b = [[]]
    flipSorroundedOXB(b)

    for l in b:
        print(l)
    print('-------------')
if __name__ == '__main__':
    test1()
    test2()
    test3()
