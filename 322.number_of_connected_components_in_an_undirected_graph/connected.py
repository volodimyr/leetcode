# Number of Connected Components in an Undirected Graph
# Topics: 'Union Find', 'Graph', 'Depth-First Search'
# Level: 'Medium'

# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1

# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2

# Constraints:

#     1 <= n <= 100
#     0 <= edges.length <= n * (n - 1) / 2

from typing import List

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        self.n = n
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def count_components(self)-> int:
        comps = set()
        for i in range(self.n):
            comps.add(self.find(i))
        return len(comps)
    
    def find(self, x: int)-> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def add(self, n1:int, n2:int):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            return
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            return
        
        self.par[p1] = p2
        self.rank[p2] += 1
        return
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in range(len(edges)):
            n1, n2 = edges[i][0], edges[i][1]
            uf.add(n1,n2)
        return uf.count_components()
