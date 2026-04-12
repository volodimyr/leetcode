# 547. Number of Provinces
# Topics: 'Depth-First Search', 'Union-Find', 'Breadth-First Search', 'Graph Theory'
# Level: 'Medium'

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

 

# Constraints:

#     1 <= n <= 200
#     n == isConnected.length
#     n == isConnected[i].length
#     isConnected[i][j] is 1 or 0.
#     isConnected[i][i] == 1
#     isConnected[i][j] == isConnected[j][i]

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
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        uf = UnionFind(ROWS)
        for r in range(ROWS):
            for c in range(r + 1, ROWS):
                if isConnected[r][c] == 1:
                    uf.add(r, c)
        
        return uf.count_components()
