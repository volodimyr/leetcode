# 159. Longest Substring with At Most Two Distinct Characters
# Topics: 'Sliding Window', 'String'
# Level: 'Medium'

# You are given a string s, return the length of the longest substring that contains at most two distinct characters.

# Note: A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "eceba"

# Output: 3

# Explanation: The substring is "ece" which its length is 3.

# Example 2:

# Input: s = "ccaabbb"

# Output: 5

# Explanation: The substring is "aabbb" which its length is 5.

# Constraints:

#     0 <= s.length <= 1,00,000
#     s consists of English letters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        letters = {}
        L = R = 0
        max_len = 0
        for c in s:
            letters[c] = letters.get(c, 0)+1
            while len(letters) > 2:
                count = letters[s[L]]
                if count > 1:
                    letters[s[L]] = count-1
                else:
                    del letters[s[L]]
                L+=1
            max_len = max(max_len, R-L+1)
            R+=1
        return max_len


