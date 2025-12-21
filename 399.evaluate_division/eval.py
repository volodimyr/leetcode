# 399. Evaluate division
# Topics: 'Depth-First Search', 'Breadth-First Search', 'Graph', 'Union Find', 'Array', 'String', 'Shortest Path'
# Level: 'Medium'

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

 

# Constraints:

#     1 <= equations.length <= 20
#     equations[i].length == 2
#     1 <= Ai.length, Bi.length <= 5
#     values.length == equations.length
#     0.0 < values[i] <= 20.0
#     1 <= queries.length <= 20
#     queries[i].length == 2
#     1 <= Cj.length, Dj.length <= 5
#     Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for (src, dst), weight in zip(equations, values):
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append((dst, weight))
            adj[dst].append((src, 1/weight))
        
        arr = []

        for src, target in queries:
            if target not in adj:
                arr.append(-1.0)
                continue

            q = deque()
            q.append((s, 1))
            res = -1

            visit = set()
            while q:
                s, weight = q.popleft()
                if s not in adj:
                    break
                if s == target:
                    res = weight
                    break
                
                visit.add(s)
                for neigh, weight1 in adj[s]:
                    if neigh not in visit:
                        q.append((neigh, weight*weight1))
            
            arr.append(res)

        return arr


        # def dfs(src, target, visit):
        #     if src not in adj:
        #         return -1
        #     if target not in adj:
        #         return -1
        #     if src == target:
        #         return 1
            
        #     visit.add(src)
        #     for neigh, weight in adj[src]:
        #         if neigh not in visit:
        #             res = dfs(neigh, target, visit)
        #             if res != -1:
        #                 return weight * res
        #     return -1
        
        # for src, target in queries:
        #     arr.append(dfs(src, target, set()))

        # return arr
