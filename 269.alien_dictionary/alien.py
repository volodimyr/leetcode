# 269. Alien Dictionary
# Topics: 'Depth-First Search', 'Topological Sort', 'Breadth-First Search', 'String', 'Hash Table'
# Level: 'Hard'

# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

#     The first letter where they differ is smaller in a than in b.
#     a is a prefix of b and a.length < b.length.

# Example 1:

# Input: ["z","o"]

# Output: "zo"

# Explanation:
# From "z" and "o", we know 'z' < 'o', so return "zo".

# Example 2:

# Input: ["hrn","hrf","er","enn","rfnn"]

# Output: "hernf"

# Explanation:

#     from "hrn" and "hrf", we know 'n' < 'f'
#     from "hrf" and "er", we know 'h' < 'e'
#     from "er" and "enn", we know get 'r' < 'n'
#     from "enn" and "rfnn" we know 'e'<'r'
#     so one possibile solution is "hernf"

# Constraints:

#     The input words will contain characters only from lowercase 'a' to 'z'.
#     1 <= words.length <= 100
#     1 <= words[i].length <= 100

from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        zp = ''.join(words)
        for char in zp:
            if char not in adj:
                adj[char] = set()

        for i in range(len(words)-1):
            prev, nxt = words[i], words[i+1]
            N = min(len(prev), len(nxt))
            diff = False
            index = 0
            for j in range(N):
                if prev[j] != nxt[j]:
                    diff = True
                    index = j
                    break
            if not diff:
                if len(prev) > len(nxt):
                    return ""
                continue
            adj[prev[index]].add(nxt[index])

        indegree = {char: 0 for char in adj}


        for k in adj:
            for v in adj[k]:
                indegree[v]+=1
    
        
        q = deque()
        for char, d in indegree.items():
            if d == 0:
                q.append(char)

        res = []
        while q:
            pop = q.popleft()
            res.append(pop)
            for node in adj[pop]:
                indegree[node]-=1
                if indegree[node] == 0:
                    q.append(node)
        
        # cycle?
        if len(res) < len(adj):
            return ""
            
        return ''.join(res)