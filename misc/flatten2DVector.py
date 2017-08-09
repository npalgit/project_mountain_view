#!/usr/bin/python
"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6]
#251
"""
class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.listIdx = 0
        self.elemIdx = 0

    def next(self):
        """
        :rtype: int
        """
        val = self.vec2d[self.listIdx][self.elemIdx]

        self.elemIdx += 1

        while self.listIdx < len(self.vec2d) and \
              (not self.vec2d[self.listIdx] or \
              self.elemIdx == len(self.vec2d[self.listIdx])):
            self.elemIdx = 0
            self.listIdx += 1

        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.listIdx < len(self.vec2d) and self.vec2d[self.listIdx] == []:
            self.listIdx += 1
        return self.listIdx < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

def test1():
    vec2d = [[1,2], [3],[4,5,6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)

def test2():
    vec2d = [[1,2], [3], [], [5,6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)

def test3():
    vec2d = [[]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)

def test4():
    vec2d = [[], [3]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
