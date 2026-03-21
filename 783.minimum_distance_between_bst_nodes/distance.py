# 783. Minimum Distance Between BST Nodes
# Topics: 'Binary Search Tree', 'Tree', 'Binary Tree', 'Depth-First Search', 'Breadth-First Search'

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:

# Input: root = [1,0,48,null,null,12,49]
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [2, 100].
#     0 <= Node.val <= 105


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
from typing import Optional

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        res = arr[len(arr)-1]
        for i in range(1, len(arr)):
            res = min(res, arr[i]-arr[i-1])
            if res == 0:
                return 0
        
        return res