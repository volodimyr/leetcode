# 156. Verify Preorder Sequence in Binary Search Tree
# Topics: 'Array', 'Stack', 'Tree', 'Binary Search Tree', 'Recursion', 'Monotonic Stack', 'Binary Tree'
# Level: 'Medium'

# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

# Example 1:

# Input: preorder = [5,2,1,3,6]

# Output: true

# Example 2:

# Input: preorder = [5,2,6,1,3]

# Output: false


# Constraints:

#     1 <= preorder.length <= 10⁴
#     1 <= preorder[i] <= 10⁴
#     All the elements of preorder are unique.

import math
from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        minv = -math.inf
        arr = []
        for n in preorder:
            while arr and arr[-1] < n:
                minv = arr.pop()

            if n <= minv:
                return False
            
            arr.append(n)
        
        return True