# 51. N-Queens
# Topics: 'Array', 'Backtracking'
# Level: 'Hard'

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:

# Input: n = 1
# Output: [["Q"]]

 

# Constraints:

#     1 <= n <= 9

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [['.' for _ in range(n)] for _ in range(n)]
                
        visitc = set()
        visitPosD = set()
        visitNegD = set()

        res = []
        def helper(r):
            if r == n:
                res.append([''.join(row) for row in arr])
                return
            for c in range(n):
                if c not in visitc and r+c not in visitPosD and r-c not in visitNegD:
                    arr[r][c] = 'Q'
                    visitc.add(c)
                    visitPosD.add(r+c)
                    visitNegD.add(r-c)

                    helper(r+1)

                    arr[r][c] = '.'
                    visitc.remove(c)
                    visitPosD.remove(r+c)
                    visitNegD.remove(r-c)
        
        helper(0)

        return res

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         default = [['.' for _ in range(n)] for _ in range(n)]
                
#         def col(r, c, matrix):
#             for i in range(r):
#                 if matrix[i][c] == 'Q':
#                     return False
#             return True

#         def diagonal(r, c, matrix, col=True):
#             while True:
#                 if min(r, c) < 0 or max(r, c) >= n:
#                     break
#                 if matrix[r][c] == 'Q':
#                     return False
#                 r -= 1
#                 if col:
#                     c += 1
#                 else:
#                     c -= 1

#             return True

#         res = []
#         def helper(r, arr):
#             if r == n:
#                 res.append([''.join(row) for row in arr])
#                 return
#             for c in range(n):
#                 if not (col(r, c, arr)  and diagonal(r-1, c-1, arr, False) and diagonal(r-1, c+1, arr, True)):
#                     continue
#                 arr[r][c] = 'Q'
#                 helper(r+1, arr)
#                 arr[r][c] = '.'
        
#         helper(0, default)

#         return res
