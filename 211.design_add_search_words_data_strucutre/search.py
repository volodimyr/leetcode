# 211. Design add and search words data structure
# Topics: 'String', 'Depth-First Search', 'Design', 'Trie'

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

#     WordDictionary() Initializes the object.
#     void addWord(word) Adds word to the data structure, it can be matched later.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

 

# Constraints:

#     1 <= word.length <= 25
#     word in addWord consists of lowercase English letters.
#     word in search consist of '.' or lowercase English letters.
#     There will be at most 2 dots in word for search queries.
#     At most 104 calls will be made to addWord and search.

class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        return self.pattern_search(self.root, 0, word)

    def pattern_search(self, next: Node, i: int, word: str) -> bool:
        if i == len(word):
            return next.word
        if word[i] == '.':
            for val in next.children.values():
                if self.pattern_search(val, i+1, word):
                    return True
            return False
        if word[i] not in next.children:
            return False
        return self.pattern_search(next.children[word[i]], i+1, word)