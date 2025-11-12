# 17. Letter Combinations of a Phone Number
# Topics: 'Hash Table', 'String', 'Backtracking'
# Level: 'Medium'

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]

 

# Constraints:

#     1 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

from typing import List


numbers_map = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        subsets = []
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                subsets.append(curStr)
                return
            for char in numbers_map[digits[i]]:
                backtrack(i+1, curStr+char)
        backtrack(0, "")
        return subsets

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         subsets = [""]
#         for digit in digits:
#             tmp = []
#             for curStr in subsets:
#                 for c in numbers_map[digit]:
#                     tmp.append(curStr+c)
#             subsets = tmp
#         return subsets