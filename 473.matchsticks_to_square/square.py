# 473. Matchsticks to Square
# Topics: 'Array', 'Dynamic Programming', 'Backtracking', 'Bit Manipulation', 'Bitmask'
# Level: 'Medium'

# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:

# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

 

# Constraints:

#     1 <= matchsticks.length <= 15
#     1 <= matchsticks[i] <= 108


from typing import List

class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        summ = sum(ms)
        if summ % 4 != 0:
            return False
        N = len(ms)

        ms.sort(reverse=True)
        sides = [0] * 4
        len_side = summ / 4

        def dfs(i):
            if i == N:
                return True
            
            for j in range(len(sides)):
                if sides[j] + ms[i] <= len_side:
                    sides[j] += ms[i] 
                    if dfs(i+1):
                        return True
                    sides[j] -= ms[i]

                if sides[j] == 0:
                    break

            return False
        
        return dfs(0)

# class Solution:
#     def makesquare(self, ms: List[int]) -> bool:
#         summ = sum(ms)
#         if summ % 4 != 0:
#             return False
#         N = len(ms)

#         from functools import lru_cache
#         @lru_cache(None)
#         def dfs(i, left, right, up, down):
#             if i == N:
#                 return left == right == up == down
            
#             for j in range(i, N):
#                 return (
#                     dfs(j+1, left+ms[j], right, up, down) or
#                     dfs(j+1, left, right+ms[j], up, down) or
#                     dfs(j+1, left, right, up+ms[j], down) or
#                     dfs(j+1, left, right, up, down+ms[j]))
        
#         return dfs(0, 0, 0, 0, 0)