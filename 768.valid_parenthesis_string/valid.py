# 678. Valid Parenthesis String
# Topics: 'String', 'Dynamic Programming', 'Stack', 'Greedy'
# Level: 'Medium'

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "(*)"
# Output: true

# Example 3:

# Input: s = "(*))"
# Output: true

 

# Constraints:

#     1 <= s.length <= 100
#     s[i] is '(', ')' or '*'.

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterix = []

        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                asterix.append(i)
            else:
                if stack:
                    stack.pop()
                elif not asterix:
                    return False
                else:
                    asterix.pop()
        
        while stack:
            if not asterix:
                return False
            if asterix[-1] < stack[-1]:
                return False
            stack.pop()
            asterix.pop()
        
        return True
        
