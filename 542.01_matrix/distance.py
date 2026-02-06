# 542. 01 Matrix
# Level: 'Medium'
# Topics: 'Array', 'Dynamic Programming', 'Matrix', 'Breadth-First Search'

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

 

# Example 1:

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

 

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 104
#     1 <= m * n <= 104
#     mat[i][j] is either 0 or 1.
#     There is at least one 0 in mat.

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        drs = [[1,0],[0,1],[-1, 0],[0,-1]]
        ROWS, COLS = len(mat), len(mat[0])

        q = deque()

        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                    visit.add((r,c))
        
        while q:
            r, c, d = q.popleft()
            mat[r][c] = d
            
            for dr, dc in drs:
                ndr, ndc = dr+r, dc+c
                if min(ndr,ndc) < 0:
                    continue
                if ndr >= ROWS or ndc >= COLS:
                    continue
                if (ndr,ndc) not in visit:
                    q.append((ndr,ndc,d+1))
                    visit.add((ndr,ndc))
        
        return mat