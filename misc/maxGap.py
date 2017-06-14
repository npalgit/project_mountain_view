#!/usr/bin/python
"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range
#164

REDO:Trick here is radix sort
"""
def mg(nums):
    if len(nums) < 2: return 0
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

    mg = 0
    for i in range(1, len(nums)):
        mg = max(mg, nums[i]-nums[i-1])

    return mg

def test1():
    nums = [170, 45, 75, 90, 802, 2, 24, 66]
    print(mg(nums))

if __name__ == '__main__':
    test1()
