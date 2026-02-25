# 343. Integer Break
# Topics: 'Dynamic Programming', 'Math'
# LeveL: 'Medium'

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 

# Constraints:

#     2 <= n <= 58

class Solution:
    def integerBreak(self, target: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(x):
            if x == 1:
                return 0
            res = 0
            for j in range(1, x):
                res = max(res, j * (x-j), j * dfs(x-j))
            
            return res
        
        return dfs(target)