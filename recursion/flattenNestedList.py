#!/usr/bin/python
"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6]
#341
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedIterator(object):
    """
    Below leetcode accepted answer
    """
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []
        self.flatten(nestedList)
        self.idx = 0

    def flatten(self, list):
        for itm in list:
            if itm.isInteger():
                self.res.append(itm.getInteger())
            else:
                self.flatten(itm.getList())

    def next(self):
        """
        :rtype: int
        """
        val = self.res[self.idx]
        self.idx += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.res)

# ------------- alternative implementation -----------
# implementation below does not require special DS, and returns
# the entire list rather than nextIterator
def flattenNested(nestedList):
    flattened = []
    dfs(nestedList, flattened)
    return flattened

def dfs(list, flattened):
    for itm in list:
        if type(itm) is int:
            flattened.append(itm)
        else:
            dfs(itm, flattened)

def test1():
    nestedList = [[1, [3, 4, 5], 1],2,[1,1]]
    print(flattenNested(nestedList))

if __name__ == '__main__':
    test1()
