#!/usr/bin/python
"""
Given an array for example: [-1, -2, 1, 9, 5, 13, 0], find the smallest positie integer value
that is not in the list. For the example above, it would be 2.
"""
def smallestPostiveIntegerNotInList(list):
    # Pass one: swap value(list[i]) with index(list[i]-1), if the following condition met:
    # index(list[i]-1) within bound of list, we are not swapping with the itself or same value.
    #
    # The basic logic is that the first pass tries to put the list element in its repective
    # order such that list[i]-1 = i
    # if possible, we bascially want to ensure list[i]-1  = i
    i = 0
    while i < len(list):
        val = list[i]

        if val >0 and val <= len(list) and (i != val-1) and (list[i] != list[val-1]):
            swap(i, val-1, list)
        else:
            i += 1

    # Pass two: go through the list, find the first element such taht list[i] != i+1
    for i in xrange(len(list)):
        if list[i] != i+1:
            return i+1

def swap(i, j, list):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

def main():
    list = [-1, -2, 1, 9, 5, 13, 0]
    rslt = smallestPostiveIntegerNotInList(list)
    assert(rslt == 2)

    list = [-3, -4, 9, 4, 6, 2, 1, 3, 5]
    rslt = smallestPostiveIntegerNotInList(list)
    assert(rslt == 7)

    list = [-3, -4, -3, -3, -3, -3, -3, -3, -3]
    rslt = smallestPostiveIntegerNotInList(list)
    assert(rslt == 1)

    list = [1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 4, 4, 4]
    rslt = smallestPostiveIntegerNotInList(list)
    assert(rslt == 5)

# run main method
main()
print("passed all tests")
