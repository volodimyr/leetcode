# 205. Isomorphic Strings
# Topics: 'Hash Table', 'String'

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

#     Mapping 'e' to 'a'.
#     Mapping 'g' to 'd'.

# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

#     1 <= s.length <= 5 * 104
#     t.length == s.length
#     s and t consist of any valid ascii character.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        
        ms, mt = {}, {}
        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]] = i
            if t[i] not in mt:
                mt[t[i]] = i
            
            if mt[t[i]] != ms[s[i]]:
                return False
        
        return True