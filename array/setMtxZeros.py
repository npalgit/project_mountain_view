#!/usr/bin/python
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#73
"""
def setMtxZeros(mtx):
    """
    60% performance
    """
    ncols = len(mtx[0])
    nrows = len(mtx)
    f_row_s, f_col_s = False, False

    for c_idx in range(ncols):
        if mtx[0][c_idx] == 0:
            f_row_s = True
            break

    for r_idx in range(nrows):
        if mtx[r_idx][0] == 0:
            f_col_s = True
            break

    for i in range(1, nrows):
        for j in range(1, ncols):
            if mtx[i][j] == 0:
                mtx[0][j] = 0
                mtx[i][0] = 0

    for c_idx in range(1, ncols):
        if mtx[0][c_idx] == 0: nullcol(c_idx, mtx)

    for r_idx in range(1, nrows):
        if mtx[r_idx][0] == 0: nullrow(r_idx, mtx)
    if f_row_s: nullrow(0, mtx)
    if f_col_s: nullcol(0, mtx)

def nullrow(r_idx, mtx):
    for j in range(len(mtx[0])):
        mtx[r_idx][j] = 0

def nullcol(c_idx, mtx):
    for i in range(len(mtx)):
        mtx[i][c_idx] = 0

def test1():
    mtx = [[0,1]]
    setMtxZeros(mtx)
    for row in mtx:
        print(row)
    print('---------')

def test2():
    mtx = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    setMtxZeros(mtx)
    for row in mtx:
        print(row)
    print('---------')

def test3():
    mtx = [[1,0]]
    setMtxZeros(mtx)
    for row in mtx:
        print(row)
    print('---------')

def test4():
    mtx = [[-1],[2],[3]]
    setMtxZeros(mtx)
    for row in mtx:
        print(row)
    print('---------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
