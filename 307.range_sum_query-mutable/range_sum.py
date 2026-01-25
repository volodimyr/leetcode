# 307. Range Sum Query- Mutable
# Topics: 'Array', 'Divide and Conquer', 'Design', 'Binary Indexed Tree', 'Segment Tree'
# Level: 'Medium'

# Given an integer array nums, handle multiple queries of the following types:

#     Update the value of an element in nums.
#     Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

# Implement the NumArray class:

#     NumArray(int[] nums) Initializes the object with the integer array nums.
#     void update(int index, int val) Updates the value of nums[index] to be val.
#     int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 

# Example 1:

# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

 

# Constraints:

#     1 <= nums.length <= 3 * 104
#     -100 <= nums[i] <= 100
#     0 <= index < nums.length
#     -100 <= val <= 100
#     0 <= left <= right < nums.length
#     At most 3 * 104 calls will be made to update and sumRange.

from typing import List

class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.right = None
        self.left = None
        self.L = L
        self.R = R

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums)-1)
    
    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.total = root.left.total + root.right.total
        return root
        
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.total = val
            return
        M = (root.L+root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.total = root.left.total + root.right.total

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)
    
    def query_helper(self, root, L, R):
        if root.R <= R and L <= root.L:
            return root.total
        if R < root.L or L > root.R:
            return 0
        return self.query_helper(root.right, L, R) + self.query_helper(root.left, L, R)

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)
