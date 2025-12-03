# 131. Palindrome Partioning
# Topics: 'Backtracking', 'String'
# Level: 'Medium'

# Given a string s, partition s such that every of the partition is a

# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]

 

# Constraints:

#     1 <= s.length <= 16
#     s contains only lowercase English letters.


from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(L, R)->bool:
            while L < R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            return True

        def backtrack(i: int):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if palindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()

        res = []
        part = []
        backtrack(0)
        return res