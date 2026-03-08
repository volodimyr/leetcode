# 441. Arranging Coins
# Topics: 'Math', 'Binary Search'

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

 

# Constraints:

#     1 <= n <= 231 - 1


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        l, r = 1, n
        res = 0
        while l <= r:
            m = (l + r) // 2
            steps = (m * (m + 1)) // 2
            if steps > n:
                r = m - 1
            else:
                res = max(res, m)
                l = m + 1
        
        return res
    
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         if n <= 2:
#             return 1
        
#         prev = 0
#         cur = 0
#         while prev + 1 + cur <= n:
#             prev += 1
#             cur += prev 
        
#         return prev
