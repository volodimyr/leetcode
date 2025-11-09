# 567. Permutation in string
# Topics: 'String', 'Sliding Window', 'Two Pointers', 'Hash Table'
# Level: 'Medium'

# Given two strings s1 and s2, return true if s2 contains a

# of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

 

# Constraints:

#     1 <= s1.length, s2.length <= 104
#     s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target  = [0]*26
        for c in s1:
            target[ord(c) - ord('a')]+=1

        s2count = [0]*26
        k = len(s1)
        for i in range (len(s2)):
            s2count[ord(s2[i]) - ord('a')]+=1
            if i+1 < k:
                continue
            if i+1 > k:
                s2count[ord(s2[i-k]) - ord('a')]-=1
            if target == s2count:
                return True
        return False