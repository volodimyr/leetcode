
# 3711. 
# Topics: 'Array', 'Heap (Priority Queue)', 'Greedy'
# Level: 'Medium'

# You are given an integer array transactions, where transactions[i] represents the amount of the iᵗʰ transaction:

#     A positive value means money is received.

#     A negative value means money is sent.

# The account starts with a balance of 0, and the balance must never become negative. Transactions must be considered in the given order, but you are allowed to skip some transactions.

# Return an integer denoting the maximum number of transactions that can be performed without the balance ever going negative.

# Example 1:

# Input: transactions = [2,-5,3,-1,-2]

# Output: 4

# Explanation: One optimal sequence is [2, 3, -1, -2], balance: 0 → 2 → 5 → 4 → 2.

# Example 2:

# Input: transactions = [-1,-2,-3]

# Output: 0

# Explanation: All transactions are negative. Including any would make the balance negative.

# Example 3:

# Input: transactions = [3,-2,3,-2,1,-1]

# Output: 6

# Explanation: All transactions can be taken in order, balance: 0 → 3 → 1 → 4 → 2 → 3 → 2.

# Constraints:

#     1 <= transactions.length <= 10⁵
#     -10⁹ <= transactions[i] <= 10⁹

import heapq
from typing import List

class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        neg_heap = []

        balance = 0
        count = 0
        for t in transactions:
            balance += t
            count += 1
            if t < 0:
                heapq.heappush(neg_heap, t)
            
            if balance < 0:
                balance -= heapq.heappop(neg_heap)
                count -= 1
        
        return count