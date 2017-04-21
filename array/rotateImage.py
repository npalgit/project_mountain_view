#!/usr/bin/python
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

#48
"""
def rotateImage(img):
    """
    81% -> 21% performance
    """
    end_idx = len(img)-1
    l, r = 0, end_idx

    while l < r:
        for i in range(l, r):
            tmp = img[l][i]
            # top => right
            img[i][r], tmp = tmp, img[i][r]

            # right => bottom
            img[r][end_idx-i], tmp = tmp, img[r][end_idx-i]

            # bottom => left
            img[end_idx-i][l], tmp = tmp, img[end_idx-i][l]

            # left => top
            img[l][i] = tmp

        l += 1
        r -= 1

def test1():
    img = [[1, 2, 3, 4], \
           [5, 6, 7, 8], \
           [9, 10, 11, 12], \
           [13, 14, 15, 16]]

    rotateImage(img)

    for r in img:
        print(r)

if __name__ == '__main__':
    test1()
