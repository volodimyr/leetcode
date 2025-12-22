# 310. Minimum height trees
# Topics: 'Breadth-First Search', 'Depth-First Search', 'Graph', 'Topological Sort'
# Level: 'Medium'

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

# Example 1:

# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:

# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

 

# Constraints:

#     1 <= n <= 2 * 104
#     edges.length == n - 1
#     0 <= ai, bi < n
#     ai != bi
#     All the pairs (ai, bi) are distinct.
#     The given input is guaranteed to be a tree and there will be no repeated edges.

from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edgecount = {}
        leaves = deque()
        for v, neighs in adj.items():
            if len(neighs) == 1:
                leaves.append(v)
            edgecount[v] = len(neighs)
        
        while leaves:
            if n <= 2:
                break
            for _ in range (len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neigh in adj[leaf]:
                    edgecount[neigh] -= 1
                    if edgecount[neigh] == 1:
                        leaves.append(neigh)
        return list(leaves)





    # Bruteforce
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     adj = {i : [] for i in range(n)}
    #     for src, dst in edges:
    #         adj[src].append(dst)
    #         adj[dst].append(src)
        
    #     def dfs(node, par):
    #         height = 0
    #         for neigh in adj[node]:
    #             if neigh == par:
    #                 continue
    #             height = max(height, 1 + dfs(neigh, node))
    #         return height

    #     res = []
    #     minh = n
    #     for i in range(n):
    #         height = dfs(i, i)
    #         if minh == height:
    #             res.append(i)
    #         elif height < minh:
    #             minh = height
    #             res = [i]
    #     return res


