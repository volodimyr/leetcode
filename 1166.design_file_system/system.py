# 1166. Design File System
# Topics: 'Hash Table', 'Design', 'Trie', 'String'
# Level: 'Medium'

# You are asked to design a file system that allows you to create new paths and associate them with different values.

# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/neetcode" and "/neetcode/problems" are valid paths while an empty string "" and "/" are not.

# Implement the FileSystem class:

#     bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.

#     int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

# Example 1:

# Input:
# ["FileSystem","createPath","get"]
# [[],["/a",1],["/a"]]

# Output:
# [null,true,1]

# Explanation:
# FileSystem fileSystem = new FileSystem();
# fileSystem.createPath("/a", 1); // return true
# fileSystem.get("/a"); // return 1

# Example 2:

# Input:
# ["FileSystem","createPath","createPath","get","createPath","get"]
# [[],["/neet",1],["/neet/code",2],["/neet/code"],["/c/d",1],["/c"]]

# Output:
# [null,true,true,2,false,-1]

# Explanation:
# FileSystem fileSystem = new FileSystem();
# fileSystem.createPath("/neet", 1); // return true
# fileSystem.createPath("/neet/code", 2); // return true
# fileSystem.get("/neet/code"); // return 2
# fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
# fileSystem.get("/c"); // return -1 because this path doesn't exist.


# Constraints:

#     2 <= path.length <= 100
#     1 <= value <= 10⁹
#     Each path is valid and consists of lowercase English letters and '/'.
#     At most 10⁴ calls in total will be made to createPath and get

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value) if self.trie.validate(path) else False

    def get(self, path: str) -> int:
        return self.trie.get(path) if self.trie.validate(path) else -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def validate(self, path: str):
        if path == "/" or path == "":
            return False
        steps = path.split('/')
        for step in steps[1:]:
            if step == '' or step == '/':
                return False
        return True

    def insert(self, path: str, value: int):
        cur = self.root
        steps = path.split('/')[1:]
        N = len(steps)

        for i in range(N-1):
            step = steps[i]
            if step not in cur.ch:
                return False
            cur = cur.ch[step]

        last = steps[N-1]
        if last in cur.ch:
            return False

        cur.ch[last] = TrieNode()    
        cur.ch[last].val = value
        return True
    
    def get(self, path: str):
        cur = self.root
        for step in path.split("/")[1:]:
            if step not in cur.ch:
                return -1
            cur = cur.ch[step]
        return cur.val

class TrieNode:
    def __init__(self):
        self.ch = {}
        self.val = -1