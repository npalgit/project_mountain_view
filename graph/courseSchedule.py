#!/usr/bin/python
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
i it possible for you to finish all courses?
For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
#207

REDO: for practice all the solutions
"""
from collections import deque

def canFinishBFSTopology(n, prereqs):
    """
    Standard lc bfs topological sort collections. It can be
    slower than my dfs solution.
    """
    if len(prereqs) <= 1: return True
    graph = [x[:] for x in [[]]*n]
    degrees = [0]*n

    for c in prereqs:
        graph[c[0]].append(c[1])
        degrees[c[1]] += 1
    q = deque()
    count = 0
    for idx, itm in enumerate(degrees):
        if itm == 0:
            q.append(idx)
            count += 1

    while q:
        n_idx = q.popleft()
        for nbr_idx in graph[n_idx]:
            degrees[nbr_idx] -= 1
            if degrees[nbr_idx] == 0:
                q.append(nbr_idx)
                count += 1

    if count == n:
        return True
    return False

def canFinish(n, prereqs):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    62.92% performance
    """
    if len(prereqs) <= 1: return True
    graph = [x[:] for x in [[]]*n]
    unvisited = set([i for i in range(n)])
    visiting = set()
    visited = set()
    for c in prereqs:
        graph[c[0]].append(c[1])
    while unvisited:
        c = unvisited.pop()
        visiting.add(c)
        if not dfs(c, graph, unvisited, visiting, visited):
            return False
    return True

def dfs(c, graph, unvisited, visiting, visited):
    for next_c in graph[c]:
        if next_c in visited: continue
        if next_c in visiting: return False
        unvisited.remove(next_c)
        visiting.add(next_c)
        if not dfs(next_c, graph, unvisited, visiting, visited):
            return False
    visiting.remove(c)
    visited.add(c)
    return True

def canFinishFewerSet(n, prereqs):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    62.92% performance
    """
    if len(prereqs) <= 1: return True
    graph = [x[:] for x in [[]]*n]
    unvisited = set([i for i in range(n)])
    visited = [False]*n

    for c in prereqs:
        graph[c[0]].append(c[1])

    while unvisited:
        c = unvisited.pop()
        visited[c] = True
        if not dfsFewerSet(c, graph, unvisited, visited):
            return False
        visited[c] = False

    return True

def dfsFewerSet(c, graph, unvisited, visited):
    """
    Using one set and one array. rather than 3 sets to detect the
    cycle.
    """
    for next_c in graph[c]:
        if visited[next_c]: return False
        if next_c in unvisited: unvisited.remove(next_c)
        visited[next_c] = True
        if not dfsFewerSet(next_c, graph, unvisited, visited):
            return False
        visited[next_c] = False
    return True

def test1():
    n = 7
    prereqs = [[0, 1], [1, 3], [2, 1], [3, 2], [5, 4], [4, 6], [6, 3]]
    print(canFinish(n, prereqs))
    print(canFinishFewerSet(n, prereqs))
    print(canFinishBFSTopology(n, prereqs))
    print('---------------------')

def test2():
    n = 7
    prereqs = [[0, 1], [2, 1], [6, 2], [3, 1], [4, 3], [5, 4]]
    print(canFinish(n, prereqs))
    print(canFinishFewerSet(n, prereqs))
    print(canFinishBFSTopology(n, prereqs))
    print('---------------------')

def test3():
    n = 2
    prereqs = [[0,1],[1,0]]
    print(canFinish(n, prereqs))
    print(canFinishFewerSet(n, prereqs))
    print(canFinishBFSTopology(n, prereqs))
    print('---------------------')

def test4():
    n = 4
    prereqs = [[1,0],[2,1],[3,2],[1,3]]
    print(canFinish(n, prereqs))
    print(canFinishFewerSet(n, prereqs))
    print(canFinishBFSTopology(n, prereqs))
    print('---------------------')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
