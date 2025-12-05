# 684. Redundant connection
# Topics: 'Union Find', 'Graph', 'Breadth-First Search', 'Depth-First Search'
# Level: 'Medium'

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

 

# Constraints:

#     n == edges.length
#     3 <= n <= 1000
#     edges[i].length == 2
#     1 <= ai < bi <= edges.length
#     ai != bi
#     There are no repeated edges.
#     The given graph is connected.

from typing import List

class UnionFind:
    def __init__(self, n:int):
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def add(self, n1:int, n2:int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            # cycle
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for i in range(len(edges)):
            if not uf.add(edges[i][0], edges[i][1]):
                return [edges[i][0],edges[i][1]]
        return []