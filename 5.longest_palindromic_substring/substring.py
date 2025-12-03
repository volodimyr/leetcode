# 5. Longest Palindromic Substring
# Topics: 'String', 'Two Pointers', 'Dynamic Programming'
# Level: 'Medium'

# Given a string s, return the longest in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.


from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(L: int, R: int) -> bool:
            while L < R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            return True
        
        def backtrack(i: int, part: List[str]):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if palindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1, part)
                    part.pop()
            return
        
        res = []
        backtrack(0, [])
        longest = ""
        for i in range(len(res)):
            for j in range(len(res[i])):
                if len(res[i][j]) > len(longest):
                    longest = res[i][j]
        return longest