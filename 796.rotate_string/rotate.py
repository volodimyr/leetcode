# 796. Rotate string
# Topics: 'String', 'String Matching'

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

#     For example, if s = "abcde", then it will be "bcdea" after one shift.

 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

 

# Constraints:

#     1 <= s.length, goal.length <= 100
#     s and goal consist of lowercase English letters.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        s += s
        return goal in s
    
# bruteforce
# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
#         if s == goal:
#             return True
#         starts = []
#         for j in range(len(goal)):
#             if s[0] == goal[j]:
#                 starts.append(j)
        
#         for i in starts:
#             matched = True
#             for c in s:
#                 if c != goal[i]:
#                     matched = False
#                     break
#                 i+=1
#                 if i >= len(goal):
#                     i = 0
#             if matched:
#                 return True
#         return False