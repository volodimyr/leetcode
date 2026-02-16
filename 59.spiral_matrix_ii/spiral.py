# 59. Spiral Matrix II
# Topics: 'Math', 'Array', 'Simulation'
# Level: 'Medium'

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:

# Input: n = 1
# Output: [[1]]

 

# Constraints:

#     1 <= n <= 20

from collections import deque
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit = set()
        N = n*n
        arr = [[0 for _ in range(n)] for _ in range(n)] 
        
        q = deque()
        q.append((0,0))
        
        dr = 0
        val = 1
        while q:
            lastr, lastc = 0, 0
            for _ in range(len(q)):
                r, c = q.popleft()
                arr[r][c] = val
                val += 1
                visit.add((r,c))
                lastr, lastc = r, c
            
            while True:
                nr, nc = lastr+directions[dr][0], lastc+directions[dr][1]
                if (nr, nc) in visit:
                    break
                if min(nr, nc) < 0:
                    break
                if max(nr, nc) >= n:
                    break
                q.append((nr, nc))
                lastr, lastc = nr, nc
                
            dr += 1
            if dr > 3:
                dr = 0
        
        return arr