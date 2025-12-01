# 79. Word Search
# Topics: 'Backtracking', 'Matrix', 'Array', 'String', 'Depth-First Search'
# Level: 'Medium'

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

 

# Constraints:

#     m == board.length
#     n = board[i].length
#     1 <= m, n <= 6
#     1 <= word.length <= 15
#     board and word consists of only lowercase and uppercase English letters.

 

# Follow up: Could you use search pruning to make your solution faster with a larger board?


from typing import Counter, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        boardc = Counter()
        wordc = Counter(word)
        ROWS, COLS = len(board), len(board[0])
        starts = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                boardc[board[i][j]] += 1
                if board[i][j] == word[0]:
                    starts.add((i,j))
        for char, count in wordc.items():
            if count > boardc[char]:
                return False
        def dfs(i: int, j: int, chari: int, visited: set) -> bool:
            if chari == len(word):
                return True
            if i == ROWS or i < 0:
                return False
            if j == COLS or j < 0:
                return False
            if (i,j) in visited:
                return False
            if board[i][j] != word[chari]:
                return False
            visited.add((i,j))
            chari+=1
            found = (
                dfs(i+1, j, chari, visited) or
                dfs(i-1, j, chari, visited) or
                dfs(i, j+1, chari, visited) or
                dfs(i, j-1, chari, visited))
            if found:
                return True
            visited.remove((i,j))

        for i, j in starts:
            if dfs(i, j, 0, set()):
                return True

        return False