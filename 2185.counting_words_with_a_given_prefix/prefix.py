# 2185. Counting words with a given prefix
# Topics: 'Array', 'String', 'String Matching'

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

 

# Example 1:

# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

# Example 2:

# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length, pref.length <= 100
#     words[i] and pref consist of lowercase English letters.

from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.times = 1

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str, length: int):
        cur = self.root
        for i in range (length):
            if word[i] not in cur.children:
                cur.children[word[i]] = Node()
            else:
                cur.children[word[i]].times += 1
            cur = cur.children[word[i]]
    
    def prefix(self, pref: str) -> int:
        cur = self.root
        for char in pref:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.times

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            if len(word) >= len(pref):
                trie.insert(word, len(pref))
        return trie.prefix(pref)
