# 745. Prefix and Suffix Search
# Topics: 'Trie', 'String', 'Design', 'Hash Table', 'Array'
# Level: 'Hard'

# Design a special dictionary that searches the words in it by a prefix and a suffix.

# Implement the WordFilter class:

#     WordFilter(string[] words) Initializes the object with the words in the dictionary.
#     f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

# Example 1:

# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

 

# Constraints:

#     1 <= words.length <= 104
#     1 <= words[i].length <= 7
#     1 <= pref.length, suff.length <= 7
#     words[i], pref and suff consist of lowercase English letters only.
#     At most 104 calls will be made to the function f.

from typing import List

class TNode:
    def __init__(self):
        self.pref = {}
        self.suff = {}
        self.prefi = []
        self.suffi = []
    
    def add(self, word: str, index: int):
        cp = self
        cs = self
        L = len(word) 
        for s in word:
            if s not in cp.pref:
                cp.pref[s] = TNode()
            cp = cp.pref[s]
            cp.prefi.append(index)
        for e in word[::-1]:
            if e not in cs.suff:
                cs.suff[e] = TNode()
            cs = cs.suff[e]
            cs.suffi.append(index)

    def search(self, prefix: str, suffix: str)-> int:
        curp = self
        for p in prefix:
            if p not in curp.pref:
                return -1
            curp = curp.pref[p]
        curs = self
        for s in suffix[::-1]:
            if s not in curs.suff:
                return -1
            curs = curs.suff[s]
        
        i, j = len(curp.prefi)-1, len(curs.suffi)-1
        while i > -1 and j > -1:
            if curp.prefi[i] == curs.suffi[j]:
                return curp.prefi[i]
            if curp.prefi[i] > curs.suffi[j]:
                i-=1
            else:
                j-=1
        return -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.words = words
        self.trie = TNode()
        for i in range(len(words)):
            self.trie.add(words[i], i)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(pref,suff)