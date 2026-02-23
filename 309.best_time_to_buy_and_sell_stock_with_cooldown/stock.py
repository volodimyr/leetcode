# 309. Best Time To Buy And Sell Stock With Cooldown
# Topics: 'Array', 'Dynamic Programming'
# Level: 'Medium'

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

#     After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:

# Input: prices = [1]
# Output: 0

 

# Constraints:

#     1 <= prices.length <= 5000
#     0 <= prices[i] <= 1000

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, stock):
            if i >= len(prices):
                return 0
            if (i,stock) in memo:
                return memo[(i,stock)]
            
            res = 0
            if stock:
                sell = helper(i+2, False) + prices[i]
                buy = helper(i+1, True)
                res = max(buy, sell)
            else:
                buy = helper(i+1, True) - prices[i]
                sell = helper(i+1, False)
                res = max(buy, sell)
            memo[(i,stock)] = res
            
            return res
        
        return helper(0, False)