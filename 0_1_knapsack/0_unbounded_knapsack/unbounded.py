# Unbounded Knapsack

# Solve the Unbounded Knapsack problem.

# You are given a list of items, each with a weight and a profit, along with a backpack with a specified maximum capacity. Your goal is to calculate the maximum profit you can achieve without exceeding the backpack's capacity. You must select items such that the total weight of the items is less than or equal to the backpack's capacity. Assume you can select each item up to an unlimited number of times.

# Input:

#     profit - a list of n integers, where profit[i] represents the profit of the i-th item. (1 <= profit[i] <= 100)
#     weight - a list of n integers, where weight[i] represents the weight of the i-th item. (1 <= weight[i] <= 100)
#     capacity - an integer representing the maximum weight the backpack can hold. (1 <= capacity <= 100)

# Here, n is the number of items, where 1 <= n <= 100. You can assume that weight and profit are both the same length and only contain positive integers.

# Example 1:

# Input:
# profit = [4, 4, 7, 1]
# weight = [5, 2, 3, 1]
# capacity = 8

# Output:
# 18

# The maximum profit you can achieve is 18, by selecting the item at index 1 once, and the item at index 2 twice. The total profit is 4 + 7 + 7 = 18, and the total weight is 2 + 3 + 3 = 8, which is equal to the backpack's capacity of 8.

from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def helper(i, cap):
            if i == len(profit):
                return 0
            mx = helper(i+1, cap)
            newCap = cap - weight[i]
            if newCap >= 0:
                # including again: i not i+1
                mx = max(profit[i] + helper(i, newCap), mx)
            return mx
        return helper(0, capacity)
