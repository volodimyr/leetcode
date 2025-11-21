# 70. Climbing stairs
# Topics: 'Math', 'Dynamic Programming', 'Memoization'

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

 

# Constraints:

#     1 <= n <= 45

from typing import List

class Solution:
   # time and space O(n)
   def climbStairs(self, n: int) -> int:
      memo = [0]*(n+1)
      return self.climb(n, memo)
   
   def climb(self, n: int, memo: List[int]) -> int:
      if n <= 1:
         return 1
      if memo[n]:
         return memo[n]
      memo[n] = self.climb(n-1, memo) + self.climb(n-2, memo)
      return memo[n]

   #  bruteforce solution O(2^n)
   # def climbStairs(self, n: int) -> int:
   #    if n <= 1:
   #       return 1
   #    return self.climbStairs(n-1) +  self.climbStairs(n-2)