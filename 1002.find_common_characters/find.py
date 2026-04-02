# 1002. Find Common Characters
# Topics: 'Array', 'Hash Table', 'String'

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 100
#     words[i] consists of lowercase English letters.



from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        for c in set(words[0]):
            min_count = float('inf')
            
            for word in words:
                min_count = min(min_count, word.count(c))
            
            res.extend([c] * min_count)
        
        return res