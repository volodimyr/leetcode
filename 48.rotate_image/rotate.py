# 48. Rotate Image
# Topics: 'Array', 'Matrix', 'Math'
# Level: 'Medium'

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

 

# Constraints:

#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000


# 90 = transpose + reverse row
# 180 = reverse row + reverse column
# 270 = transpose + reverse col
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
# transpose
        for r in range(N):
            for c in range(r+1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
# reverse row
        for r in range(N):
            L, R = 0, N-1
            while L < R:
                matrix[r][L], matrix[r][R] = matrix[r][R], matrix[r][L]
                L+=1
                R-=1

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         N = len(matrix)
#         # t, b = 0, N-1
#         # while t < b:
#         #     for c in range(N):
#         #          matrix[t][c], matrix[b][c] = matrix[b][c], matrix[t][c]
#         #     t+=1
#         #     b-=1
#         matrix.reverse()


# # transpose
#         for r in range(N):
#             for c in range(r+1, N):
#                 matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        