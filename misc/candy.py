#!/usr/bin/python
"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

#135
REDO
"""
def dstrb_candy3(chdn):
    # check for out of bound
    i, j = 0, 0
    n = len(chdn)
    candy = [1]*n
    v = 1
    while j+1 < n:
        if chdn[j] < chdn[j+1]:
            v = 1
            while j+1 < n and chdn[j] <= chdn[j+1]:
                candy[j] = v
                j += 1
                if chdn[idx] != chdn[idx+1]: v += 1
            j += 1
        else:
            i = j
            while j+1 < n and chdn[j] >= chdn[j+1]:
                j += 1

            for idx in reversed(range(i, j+1)):
                candy[idx] = v
                if chdn[idx] != chdn[idx+1]: v += 1

        print(candy)
    if chdn[-2] == chdn[-1]: candy[-1] = candy[-2]
    elif chdn[-2] > chdn[-1]: candy[-1] = 1
    else: candy[-1] = candy[-2] + 1
    return sum(candy)

def dstrb_candy2(chdn):
    # check for out of bound
    i, j = 0, 1
    n = len(chdn)
    candy = [1]*n
    v = 1
    while j < n:
        # increasing
        if chdn[j-1] < chdn[j]:
            while j < n and chdn[j-1] <= chdn[j]:
                if j < n and chdn[j-1] != chdn[j]: v += 1
                candy[j] = v
                j += 1
        # decreasing
        else:
            i = j-1
            while j < n and chdn[j-1] >= chdn[j]:
                j += 1

            for idx in reversed(range(i, j)):
                candy[idx] = v
                if idx == 0 or chdn[idx-1] != chdn[idx]: v += 1
        v = 1

        print(candy)
    return sum(candy)

def dstrb_candy(chdn):
    n = len(chdn)
    l2r = [1]*n
    r2l = [1]*n
    v = 1

    for i in range(1, n):
        if chdn[i-1] < chdn[i]:
            v += 1
            l2r[i] = v
        else:
            v = 1
    v = 1
    for i in reversed(range(n-1)):
        if chdn[i] > chdn[i+1]:
            v += 1
            r2l[i] = v
        else:
            v = 1

    sum_r = 0
    test_max = [1]*n

    for i in range(n):
        sum_r += max(l2r[i], r2l[i])
        test_max[i] = max(l2r[i], r2l[i])
    print(l2r)
    print(r2l)
    print(test_max)
    return sum_r

def test1():
    chdn = [12,  4,  3, 11, 34, 34,  1, 67]
    print(dstrb_candy(chdn))

def test2():
    chdn = [5, 4, 3, 6, 6, 5, 4, 5, 4, 3]
    print(dstrb_candy(chdn))

def test3():
    chdn = [1,2,2]
    print(dstrb_candy(chdn))

if __name__ == '__main__':
    #test1()
    #test2()
    test3()
