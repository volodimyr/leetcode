# 1100. Find K-Length Substrings With No Repeated Characters
# Topics: 'Hash Table', 'String', 'Sliding Window'
# Level: 'Medium'

# Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

# Example 1:

# Input: s = "havefunonneetcode", k = 5

# Output: 6

# Explanation:

# There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.


# Example 2:

# Input: s = "home", k = 5

# Output: 0

# Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

# Constraints:

#     1 <= s.length <= 10^4
#     s consists of lowercase English letters
#     1 <= k <= 10^4

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counter = {}
        
        for i in range(k):
            c = s[i]
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        res = 0
        if len(counter) == k:
                res += 1
        for i in range(k, len(s)):
            forw = s[i]
            back = s[i-k]
            counter[back] -= 1
            if counter[back] == 0:
                del counter[back]
            if forw in counter:
                counter[forw] += 1
            else:
                counter[forw] = 1
            
            if len(counter) == k:
                res += 1
        
        return res
