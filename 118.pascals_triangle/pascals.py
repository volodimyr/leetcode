# 118. Pascal's Triangle
# Topics: 'Array', 'Dynamic Programming'

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

 

# Constraints:

#     1 <= numRows <= 30

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        if numRows == 2:
            return res

        for i in range(1, numRows-1):
            r, c = i, 0

            res1 = [1]
            while c < len(res[i])-1:
                res1.append(res[i][c] + res[i][c+1])
                c+=1
            
            res1.append(1)
            res.append(res1)
        
        return res
