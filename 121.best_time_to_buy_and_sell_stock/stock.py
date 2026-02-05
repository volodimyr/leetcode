from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        p = 0
        cur = prices[0]
        for i in range(1, len(prices)):
            if prices[i]-cur > 0:
                p = max(p, prices[i]-cur)
            else:
                cur = prices[i]
        return p