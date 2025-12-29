# 54. Spiral Matrix
# Topics: 'Array', 'Matrix', 'Simulation'
# Level: 'Medium'

# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        N = ROWS*COLS

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = j = dr = 0
        visit = set()
        res = []

        for _ in range(N):
            res.append(matrix[i][j])
            visit.add((i,j))

            ni, nj = directions[dr][0]+i, directions[dr][1]+j
            if min(nj,nj) < 0 or ni == ROWS or nj == COLS or (ni,nj) in visit:
                dr = (dr+1) % 4
                ni, nj = directions[dr][0]+i, directions[dr][1]+j
            
            i, j = ni, nj

        return res

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         ROWS, COLS = len(matrix), len(matrix[0])
#         N = ROWS*COLS

#         drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         visit = set()

#         def change_direction(dr):
#             dr+=1
#             if dr == len(drs):
#                 dr = 0
#             return dr
            
#         def next(i, j, dr):
#             dri, drj = drs[dr]
#             if i+dri < 0 or j+drj < 0 or i+dri == ROWS or j+drj == COLS or (i+dri, j+drj) in visit:
#                 return next(i, j, change_direction(dr))

#             return i+dri, j+drj ,dr

#         j = -1
#         i = dr = 0
#         res = []
#         while len(res) < N:
#             i, j, dr = next(i, j, dr)
#             visit.add((i,j))
#             res.append(matrix[i][j])

#         return res