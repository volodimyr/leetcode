# 76. Minimum Window Substring
# Topics: 'Hash Table', 'String', 'Sliding Window'
# Level: 'Hard'

# Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

 

# Constraints:

#     m == s.length
#     n == t.length
#     1 <= m, n <= 105
#     s and t consist of uppercase and lowercase English letters.

 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tarr = [0] * 58
        for ts in t:
            tarr[ord(ts)-ord('A')] += 1


        sarr = [0] * 58
        L, R = 0, 0
        res = ""
        while R < len(s):
            if not self.validate(tarr, sarr):
                sarr[ord(s[R]) - ord('A')] += 1
                R+=1
            else:
                if res == "" or len(res) > R-L:
                    res = s[L:R]
                sarr[ord(s[L]) - ord('A')] -= 1
                L+=1
                if len(res) == len(t):
                    return res
        
        while L < len(s) and self.validate(tarr, sarr):
            if res == "" or len(res) > R-L:
                res = s[L:R]
            sarr[ord(s[L]) - ord('A')] -= 1
            L+=1
            if len(res) == len(t):
                return res

        return res

    
    def validate(self, tarr, sarr):
        for i in range(len(tarr)):
            if tarr[i] > sarr[i]:
                return False
        return True