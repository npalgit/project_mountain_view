#!/usr/bin/python
"""
Implement int sqrt(int x).
Compute and return the square root of x
leetcode #69
REDDO: many smart solutions, try newton method optional
"""
def sqrt(n):
    """
    if number is too big will take forever.
    """
    d = 1
    while d*d <= n:
        d +=1

    return d-1

def sqrt_bin_search(n):
    beg = 0
    end = n
    # or  end = 46340 # the sqrt of int_max

    while beg <= end:
        mid = beg + (end-beg)/2
        mul = mid*mid
        if mul == n or (mul < n and (mid+1)*(mid+1) > n):
            return mid
        if mul < n:
            beg = mid +1
        else:
            end = mid -1

def test1():
    print(sqrt(45))
    print(sqrt_bin_search(45))
    print("----------------")

def test2():
    print(sqrt(49))
    print(sqrt_bin_search(49))
    print("----------------")

def test3():
    print(sqrt(1))
    print(sqrt_bin_search(1))
    print("----------------")

def test3():
    print(sqrt(600))
    print(sqrt_bin_search(600))
    print("----------------")

def test4():
    print(sqrt_bin_search(0x7fffffff))
    print("----------------")

if __name__ == "__main__":
    test1()
    test2()
    test3()
