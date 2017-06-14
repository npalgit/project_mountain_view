#!/usr/bin/python

def radix_sort_single(nums):
    """
    single digit radix sort
    """
    count = [0]*10
    out = [0]*len(nums)

    # create histogram
    for d in nums: count[d] += 1

    # create incremental sum including prev
    for i in range(1, len(count)):
        count[i] += count[i-1]

    for d in nums:
        count[d] -= 1
        out[count[d]] = d

    return out

def radix_sort(nums):
    """
    radix sort using counting sort as subroutine
    """
    out = [0]*len(nums)
    max_elem = max(nums)
    exp = 1

    while max_elem/exp > 0:
        count = [0]*10
        # create histogram
        for d in nums:
            count[(d/exp)%10] += 1

        # create incremental sum including prev
        for i in range(1, len(count)):
            count[i] += count[i-1]

        for d in reversed(nums):
            count[(d/exp)%10] -= 1
            out[count[(d/exp)%10]] = d

        exp *= 10
        nums, out = out, nums
    return nums

def test1():
    nums = [9, 1, 0, 3, 5, 3, 2, 4, 8, 7,9, 8, 0, 3]
    print(sort(nums))

def test2():
    nums = [170, 45, 75, 90, 802, 2, 24, 66]
    print(radix_sort(nums))

if __name__ == '__main__':
    test2()
