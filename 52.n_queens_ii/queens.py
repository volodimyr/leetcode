# 52. N-Queens II
# Topics: 'Backtracking'
# Level: 'Hard'

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:

# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

# Example 2:

# Input: n = 1
# Output: 1

 

# Constraints:

#     1 <= n <= 9


class Solution:
    def totalNQueens(self, n: int) -> int:
        arr = [['.' for _ in range(n)] for _ in range(n)]
                
        visitc = set()
        visitPosD = set()
        visitNegD = set()
        def helper(r):
            if r == n:
                return 1
            res = 0
            for c in range(n):
                if c not in visitc and r+c not in visitPosD and r-c not in visitNegD:
                    arr[r][c] = 'Q'
                    visitc.add(c)
                    visitPosD.add(r+c)
                    visitNegD.add(r-c)

                    res += helper(r+1)

                    arr[r][c] = '.'
                    visitc.remove(c)
                    visitPosD.remove(r+c)
                    visitNegD.remove(r-c)
            return res
        

        return helper(0)
