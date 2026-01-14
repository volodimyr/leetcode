# 647. Palindromic Substrings
# Topics: 'String', 'Dynamic Programming', 'Two Pointers'
# Level: 'Medium'

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

# Constraints:

#     1 <= s.length <= 1000
#     s consists of lowercase English letters.


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1
        res = 0
        def helper(L, R):
            count = 0
            while L >= 0 and R < N and s[L] == s[R]:
                count+=1
                R+=1
                L-=1
            return count
        
        for i in range(N):
            res += helper(i, i)
            res += helper(i, i+1)
        
        return res