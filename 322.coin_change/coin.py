# 322. Coin Change
# Topics: 'Array', 'Dynamic Programming', 'Breadth-First Search'
# Level: 'Medium'

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

 

# Constraints:

#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

import math
from typing import List

# bottom-up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0

        for a in range(amount+1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1+dp[a-c])
        
        return dp[amount] if dp[amount] != math.inf else -1

        # if amount == 0:
        #     return 0
        # min_steps = math.inf
        # memo = {}
        # def coin(n):
        #     if n == 0:
        #         return 0
        #     if n in memo:
        #         return memo[n]
        #     min_steps = math.inf
        #     for c in coins:
        #         if n-c >= 0:
        #             min_steps = min(1+coin(n-c), min_steps)
        #     memo[n] = min_steps
        #     return memo[n]
        # res = coin(amount)
        # return -1 if res == math.inf else res

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
        
#         cache = {}
#         def helper(amount):
#             if amount == 0:
#                 return 0
#             if amount in cache:
#                 return cache[amount]
            
#             res = 1e9
#             for c in coins:
#                 if amount-c >= 0:
#                     res = min(res, 1+helper(amount-c))
#             cache[amount] = res
#             return res

#         res = helper(amount)
#         return -1 if res == 1e9 else res
