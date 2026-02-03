# 139. Word Break
# Topics: 'Array', 'Hash Table', 'String', 'Dynamic Programming', 'Trie', 'Memoization'
# Level: 'Medium'

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

 

# Constraints:

#     1 <= s.length <= 300
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.

from typing import List

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.ch:
                cur.ch[c] = Node()
            cur = cur.ch[c]
        cur.word = True
    
    def search(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.ch:
                return False
            cur = cur.ch[c]
        return cur.word

class Node:
    def __init__(self):
        self.ch = {}
        self.word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        
        N = len(s)
        memo = {}
        def dfs(i, j):
            if j >= N+1:
                return i == N
            if (i, j) in memo:
                return memo[(i,j)]

            found = trie.search(s[i:j])
            skip = dfs(i, j+1)
            if not found:
                memo[(i,j)] = skip
                return skip

            res = skip or dfs(j, j+1)
            memo[(i,j)] = res
            return res
        
        return dfs(0, 1)

