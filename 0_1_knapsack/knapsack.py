from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i, cap):
            if i == len(profit):
                return 0
            max_profit = dfs(i+1, cap)
            new_cap = cap - weight[i]
            if new_cap >= 0:
                p = profit[i] + dfs(i+1, new_cap)
                max_profit = max(max_profit, p)
            
            return max_profit
        
        return dfs(0, capacity)