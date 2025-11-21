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
    def climbStairs(self, n: int) -> int:
      if n < 2:
         return n
      one, two = 0, 1
      i = 2
      while i <= n+1:
         tmp = two
         two = one+two
         one = tmp
         i+=1
      return two

   # def climbStairs(self, n: int) -> int:
   #    if n < 2:
   #       return n
      
   #    dp = [0, 1]
   #    i = 2
   #    while i <= n+1:
   #       tmp = dp[1]
   #       dp[1] = dp[0] + dp[1]
   #       dp[0] = tmp
   #       i+=1
   #    return dp[1]

   # time and space O(n)
   # def climbStairs(self, n: int) -> int:
   #    memo = [0]*(n+1)
   #    return self.climb(n, memo)
   
   # def climb(self, n: int, memo: List[int]) -> int:
   #    if n <= 1:
   #       return 1
   #    if memo[n]:
   #       return memo[n]
   #    memo[n] = self.climb(n-1, memo) + self.climb(n-2, memo)
   #    return memo[n]

   #  bruteforce solution O(2^n)
   # def climbStairs(self, n: int) -> int:
   #    if n <= 1:
   #       return 1
   #    return self.climbStairs(n-1) +  self.climbStairs(n-2)