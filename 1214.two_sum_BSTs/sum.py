# 1214. Two Sum BSTs
# Topics: 'Two Pointers', 'Binary Search', 'Stack', 'Tree', 'Depth-First Search', 'Binary Search Tree', 'Binary Tree'
# Level: 'Medium'

# Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

# Example 1:

# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5

# Output: true

# Explanation: 2 and 3 sum up to 5.

# Example 2:

# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18

# Output: false


# Constraints:

#     The number of nodes in each tree is in the range [1, 5000].
#     -10⁹ <= Node.val, target <= 10⁹

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        x = set()
        def dfs(root):
            if not root:
                return
            x.add(target - root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root1)

        def search(root):
            if not root:
                return False
            if root.val in x:
                return True
            if search(root.left):
                return True
            if search(root.right):
                return True
            return False
        
        return search(root2)