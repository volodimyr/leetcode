# 5. Longest Palindromic Substring
# Topics: 'Two Pointers', 'String', 'Dynamic Programming'
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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def helper(L, R):          
            while L >= 0 and R < N and s[L] == s[R]:
                L-=1
                R+=1
            return s[L+1:R]

        mx = ''
        for i in range(N):
            odd = helper(i, i)
            if len(odd) > len(mx):
                mx = odd
            even = helper(i, i+1)
            if len(even) > len(mx):
                mx = even
            if len(mx) == N:
                break
        
        return mx
    