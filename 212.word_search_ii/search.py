# 212. Word Search II
# Topics: 'Array', 'Matrix', 'Trie', 'Backtracking', 'String'
# Level: 'Hard'

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:

# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

 

# Constraints:

#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 12
#     board[i][j] is a lowercase English letter.
#     1 <= words.length <= 3 * 104
#     1 <= words[i].length <= 10
#     words[i] consists of lowercase English letters.
#     All the strings of words are unique.

from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.words = []
    
    def prefix(self, s: str) -> 'Trie':
        if s not in self.children:
            return None
        return self.children[s]

    def add(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.words.append(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        res = set()
        def search(i: int, j:int, node: Trie, visited: set):
            if i < 0 or j < 0:
                return 
            if i >= ROWS or j >= COLS:
                return 
            if (i,j) in visited:
                return
            node = node.prefix(board[i][j])
            if not node:
                return
            for w in node.words:
                res.add(w)
            # early optimisation
            node.words = []
            
            visited.add((i,j))
            search(i+1, j, node, visited)
            search(i-1, j, node, visited)
            search(i, j+1, node, visited)
            search(i, j-1, node, visited)
            visited.remove((i,j))
            
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range (COLS):
                search(i, j, trie, set())
        return list(res)

