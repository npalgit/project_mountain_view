#!/usr/bin/python
"""
Given an integer n, generate a square matrix filled with elements from 1 to n2
in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
#59
"""
def generateSpiralMtx(n):
    mtx = [x[:] for x in [[0]*n]*n]
    it = 1
    l, r, t, b = 0, n-1, 0, n-1

    while it <= n*n:
        # top row
        for i in range(l, r+1):
            mtx[t][i] = it
            it += 1

        t += 1

        # right col
        for i in range(t, b+1):
            mtx[i][r] = it
            it += 1
        r -= 1

        # bottom row
        for i in reversed(range(l, r+1)):
            mtx[b][i] = it
            it += 1
        b -= 1

        for i in reversed(range(t, b+1)):
            mtx[i][l] = it
            it += 1
        l += 1

    return mtx

def test1():
    mtx = generateSpiralMtx(3)
    for row in mtx:
        print(row)
    print('----------------')

def test2():
    mtx = generateSpiralMtx(4)
    for row in mtx:
        print(row)

def test3():
    mtx = generateSpiralMtx(5)
    for row in mtx:
        print(row)
    print('----------------')

def test4():
    mtx = generateSpiralMtx(2)
    for row in mtx:
        print(row)
    print('----------------')

def test5():
    mtx = generateSpiralMtx(1)
    for row in mtx:
        print(row)
    print('----------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
