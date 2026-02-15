# 270. Closest Binary Search Tree Value
# Topics: 'Binary Search', 'Tree', 'Depth-First Search', 'Binary Search Tree', 'Binary Tree'

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

# Example 1:

# Input: root = [4,2,5,1,3], target = 3.714286

# Output: 4

# Example 2:

# Input: root = [1], target = 4.428571

# Output: 1


# Constraints:

#     The number of nodes in the tree is in the range [1, 10⁴].
#     0 <= Node.val <= 10⁹
#     -10⁹ <= target <= 10⁹

import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = [math.inf]
        def dfs(root):
            if not root:
                return 
            if root.val == target:
                res[0] = root.val
                return 
            if abs(root.val - target) < abs(res[0]-target):
                res[0] = root.val
            if target < root.val:
                dfs(root.left)
            else:
                dfs(root.right)

        dfs(root)

        return res[0]