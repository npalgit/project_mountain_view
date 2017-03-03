#!/usr/bin/python
"""
Spiral matrix print
leetcode #54
"""
def spiralP(mtx):
    rslt = []
    if not mtx:
        return rslt
    l, r, t, b = 0, len(mtx[0])-1, 0, len(mtx)-1
    i, j = l, t

    while l <= r and t <= b: 

        j = l
        while j <= r:
            rslt.append(mtx[t][j])
            j += 1
        t += 1

        i = t
        while i <= b:
            rslt.append(mtx[i][r])
            i += 1
        r -= 1

        j = r
        while t <= b and j >= l:
            rslt.append(mtx[b][j])
            j -= 1
        b -= 1
        
        i = b
        while l <= r and  i >= t:
            rslt.append(mtx[i][l])
            i -= 1
        l += 1

    return rslt

def test1():
    mtx = [ \
           [1, 2, 3, 4, 5], \
           [6, 7, 8, 9, 10], \
           [11, 12, 13, 14, 15],\
          ]
    print(spiralP(mtx))
    print("---------------------")

def test2():
    mtx = [[1, 2, 3, 4, 5, 6]]
    print(spiralP(mtx))
    print("---------------------")

def test3():
    mtx = [[1], [2], [3], [4], [5]]
    print(spiralP(mtx))
    print("---------------------")

def test4():
    mtx =[]

if __name__ == "__main__":
    test1()
    test2()
    test3()
