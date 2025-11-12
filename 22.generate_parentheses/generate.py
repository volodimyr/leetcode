# 22. Generate parentheses
# Topics: 'String', 'Backtracking', 'Dynamic Programming'
# Level: 'Medium'

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]
 
# Constraints:

#     1 <= n <= 8

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl, curStr):
            if len(curStr) == 2*n:
                subsets.append(curStr)
                return
            if op < n:
                backtrack(op+1, cl, curStr+'(')
            if cl < op:
                backtrack(op, cl+1, curStr+')')

        subsets = []
        backtrack(0, 0, "")
        return subsets