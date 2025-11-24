# Longest Substring with at most K distinct Charecters
# Topics: 'Sliding Window', 'String'
# Level: 'Medium'

# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "eceba", k = 2

# Output: 3

# Explanation: The substring is "ece" with length 3.

# Example 2:

# Input: s = "aa", k = 1

# Output: 2

# Explanation: The substring is "aa" with length 2.

# Constraints:

#     1 <= s.length <= 5 * 10^4
#     0 <= k <= 50

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        L = R = 0
        chars = defaultdict(int)
        res = 0
        while R < len(s):
            chars[s[R]]+=1
            while len(chars) > k:
                chars[s[L]]-=1
                if chars[s[L]] == 0:
                    del chars[s[L]]
                L+=1
            R+=1
            res = max(res, R-L)
        return res
