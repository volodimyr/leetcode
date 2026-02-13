# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Topics: 'Sorting', 'Graph Theory', 'Union Find', 'Minimum Spanning Tree', 'Strongly Connected Component'
# Level: 'Hard'

# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

 

# Example 1:

# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

# Example 2:

# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

 

# Constraints:

#     2 <= n <= 100
#     1 <= edges.length <= min(200, n * (n - 1) / 2)
#     edges[i].length == 3
#     0 <= ai < bi < n
#     1 <= weighti <= 1000
#     All pairs (ai, bi) are distinct.




import math
from typing import List

class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.par = {}
        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
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

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[i, n1, n2, w] for i, (n1, n2, w) in enumerate(edges)]
        critical = []
        pseudo = []
        edges.sort(key=lambda x: x[3])

        def find_mst(exclude=-1, include=-1):
            weight = 0
            count = 0
            u = UnionFind(n)

            if include != -1:
                _, n1, n2, w = edges[include]
                weight += w
                count += 1
                u.union(n1, n2)            
           
            for i, (_, n1, n2, w) in enumerate(edges):
                if i == exclude:
                    continue
                if u.union(n1, n2):
                    weight += w
                    count += 1
                if count == n - 1:
                    break

            return weight if count == n-1 else math.inf

        base_weight = find_mst()
        
        for i in range(len(edges)):
            if find_mst(exclude=i) > base_weight:
                critical.append(edges[i][0])
            elif find_mst(include=i) == base_weight:
                pseudo.append(edges[i][0])
        
        return [critical, pseudo]


