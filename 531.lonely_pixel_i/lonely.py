# 531. Lonely Pixel I
# Topics:
# LeveL: 'Medium'

# Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

# A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example 1:

# Input: picture = [
#                  ["W","W","B"],
#                  ["W","B","W"],
#                  ["B","W","W"]]

# Output: 3

# Explanation: All the three 'B's are black lonely pixels.

# Example 2:

# Input: picture = [
#                  ["B","B","B"],
#                  ["B","B","W"],
#                  ["B","B","B"]]

# Output: 0

# Constraints:

#     m == picture.length
#     n == picture[i].length
#     1 <= m, n <= 500
#     picture[i][j] is 'W' or 'B'.

from typing import List

class Solution:
    def findLonelyPixel(self, p: List[List[str]]) -> int:
        rows = {}
        cols = {}

        ROWS, COLS = len(p), len(p[0])

        for r in range(ROWS):
            count = 0
            for c in range(COLS):
                if p[r][c] == 'B':
                    count+=1
                if count > 1:
                    break
            
            if count <= 1:
                rows[r] = True
            else:
                rows[r] = False
        
        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                if p[r][c] == 'B':
                    count+=1
                if count > 1:
                    break
            
            if count <= 1:
                cols[c] = True
            else:
                cols[c] = False
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if p[r][c] == 'B' and rows[r] and cols[c]:
                    res +=1

        return res 