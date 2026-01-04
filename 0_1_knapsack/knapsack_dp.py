from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity
        cache = [[0]*(COLS+1) for _ in range(ROWS)]
        
        for r in range(ROWS):
            cache[r][0] = 0
        
        for c in range(COLS+1):
            if weight[0] <= c:
                cache[0][c] = profit[0]
        
        for r in range(1, ROWS):
            for c in range(1, COLS+1):
                skip = cache[r-1][c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + cache[r-1][c-weight[r]]
                
                cache[r][c] = max(include, skip)
        
        return cache[ROWS-1][COLS]