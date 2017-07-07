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

def sqrt_r2(n):
    """
    Finding the exact number or the number just greater than the mid.
    Why we need to do `beg-1` in the end
    """
    beg = 0
    end = n

    while beg < end:
        mid = beg + (end-beg)/2
        mul = mid*mid
        if mul < n:
            beg = mid+1
        else:
            end = mid

    return beg if beg*beg == n else beg-1

def sqrt_r(n):
    """
    by doing mid = (beg+end+1)/2. we always make sure the right half is shorter or
    equal to the left half. the right half started with mid.
    Since we are only closing in from the right `end = mid-1`
    we need to choose the mid to be a little bigger than the traditional sense
    so not to stuck in loop.

    e.g. 

    idx 4 5
    n  [6 7]
    
    traditional:
        mid = (4+5)/2 = 4
        beg = mid
        end = 5
        This loops forever and does not change.

    Current:
        mid = (4+5+1)/2 = 5
        beg = mid
        end = 5
        beg = end = 5
        return 7

    """
    beg = 0
    end = n
    while beg < end:
        mid = (beg+end+1)/2
        mul = mid*mid
        if mul > n:
            end = mid-1
        else:
            beg = mid
    return beg

def test1():
    print(sqrt_r(45))
    print(sqrt_bin_search(45))
    print("----------------")

def test2():
    print(sqrt_r(49))
    print(sqrt_bin_search(49))
    print("----------------")

def test3():
    print(sqrt_r(1))
    print(sqrt_bin_search(1))
    print("----------------")

def test3():
    print(sqrt_r(600))
    print(sqrt_bin_search(600))
    print("----------------")

def test4():
    print(sqrt_bin_search(0x7fffffff))
    print("----------------")

if __name__ == "__main__":
    test1()
    test2()
    test3()
