
from typing import List


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        def helper(root, key, val):
            if not root:
                return Node(key, val)
            if root.key == key:
                root.val = val
            elif root.key < key:
                root.right = helper(root.right, key, val)
            else:
                root.left = helper(root.left, key, val)
            return root

        self.root = helper(self.root, key, val)


    def get(self, key: int) -> int:
        def helper(root, key):
            if not root:
                return -1  
            if key == root.key:
                return root.val
            if key > root.key:
                return helper(root.right, key)
            else:
                return helper(root.left, key)

        return helper(self.root, key)

    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val



    def remove(self, key: int) -> None:
        def find_min(root):
            cur = root
            while cur.left:
                cur = cur.left
            return cur

        def helper(root, key):
            if not root:
                return root
            if root.key < key:
                root.right = helper(root.right, key)
            elif root.key > key:
                root.left = helper(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                min_node = find_min(root.right)
                root.key, root.val = min_node.key, min_node.val
                root.right = helper(root.right, min_node.key)
            return root
            
        self.root = helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.key)
            helper(root.right)
        
        helper(self.root)
        return res
