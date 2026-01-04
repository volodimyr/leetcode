from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity
        cache = [[-1]*(COLS+1) for _ in range(ROWS)]
        def dfs(i, cap):
            if i == len(profit):
                return 0
            if cache[i][cap] != -1:
                return cache[i][cap]
            cache[i][cap] = dfs(i+1, cap)
            new_cap = cap - weight[i]
            if new_cap >= 0:
                p = profit[i] + dfs(i+1, new_cap)
                cache[i][cap] = max(cache[i][cap], p)
            
            return cache[i][cap]
        
        return dfs(0, capacity)