# 1462. Course schedule IV
# Topics: 'Depth-First Search', 'Breadth-First Search', 'Graph', 'Topological Sort'
# Level: 'Medium'

from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: set() for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].add(dst)
        
        reachable = {}
        def dfs(n: int):
            if n in reachable:
                return reachable[n]
            path = set(adj[n])
            for e in adj[n]:
                path.update(dfs(e))
            reachable[n] = path
            return reachable[n]
        
        for n in range(numCourses):
            dfs(n)

        res = []
        for src, dep in queries:
            if dep in reachable[src]:
                res.append(True)
            else:
                res.append(False)

        return res 
