class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s)-1
        while L < R:
            while L < R and not s[L].isalnum():
                L+=1
            while L < R and not s[R].isalnum():
                R-=1
            if s[R] != s[L]:
                return False
            R-=1
            L+=1

        return True
# ()'a' <= s[L] <= 'z') or ()'0' <= s[L] <= '9') == isalnum()