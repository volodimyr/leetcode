# 387. First Unique Character in a String
# Topics: 'Hash Table', 'String', 'Queue', 'Counting'

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = (0, i)
            count, index = m[s[i]]
            count+=1
            m[s[i]] = (count, index)

        for c in s:
            if m[c][0] == 1:
                return m[c][1]

        return -1