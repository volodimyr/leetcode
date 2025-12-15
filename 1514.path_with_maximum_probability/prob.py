# 1514. Path with Maximum Probability
# Topics: 'Array', 'Graph', 'Heap (Pririty Queue)', 'Shortest Path'
# Level: 'Medium'

# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:

# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

# Example 2:

# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000

# Example 3:

# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.

 

# Constraints:

#     2 <= n <= 10^4
#     0 <= start, end < n
#     start != end
#     0 <= a, b < n
#     a != b
#     0 <= succProb.length == edges.length <= 2*10^4
#     0 <= succProb[i] <= 1
#     There is at most one edge between every two nodes.

import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i : [] for i in range(n)}
        for edge, succ in zip(edges, succProb):
            adj[edge[0]].append((edge[1], succ))
            adj[edge[1]].append((edge[0], succ))
        
        maxheap = [(float(-1), start_node)]
        highestProbability = {}
        while maxheap:
            prob1, src1 = heapq.heappop(maxheap)
            if src1 in highestProbability:
                continue
            highestProbability[src1] = prob1
            if src1 == end_node:
                return -prob1
            for src2, prob2 in adj[src1]:
                if src2 not in highestProbability:
                    heapq.heappush(maxheap, (prob2*prob1, src2))
        
        if end_node not in highestProbability:
            return float(0)
        prob = highestProbability[end_node]
        return -prob
    
# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
#         adj = {i : [] for i in range(n)}
#         for edge, succ in zip(edges, succProb):
#             adj[edge[0]].append((edge[1], succ))
#             adj[edge[1]].append((edge[0], succ))
        
#         maxheap = [(-1, start_node)]
#         highest_prob = [0.0] * n
#         while maxheap:
#             prob1, src1 = heapq.heappop(maxheap)
#             prob1 = -prob1
#             if prob1 < highest_prob[src1]:
#                 continue
#             if src1 == end_node:
#                 return prob1
#             for src2, prob2 in adj[src1]:
#                 n_prob = prob1*prob2
#                 if n_prob > highest_prob[src2]:
#                     highest_prob[src2] = n_prob
#                     heapq.heappush(maxheap, (-n_prob, src2))
#         return highest_prob[end_node]
