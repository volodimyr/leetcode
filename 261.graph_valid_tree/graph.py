# 261. Graph valid tree
# Topics: 'Graph', 'Union Find', 'Depth-First Search'
# Level: 'Medium'

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# Output:
# true

# Example 2:

# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Output:
# false

# Note:

#     You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Constraints:

#     1 <= n <= 100
#     0 <= edges.length <= n * (n - 1) / 2

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        u = UnionFind(n)
        for n1, n2 in edges:
            if not u.add(n1,n2):
                return False

        return True

class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.par = {}
        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    
    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def add(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            return True
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            return True

        self.par[p1] = p2
        self.rank[p2] += 1
        return True 