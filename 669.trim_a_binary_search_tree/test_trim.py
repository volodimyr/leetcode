import unittest
from typing import Optional
from trim import Solution,TreeNode

# --- Helper function for testing ---
def tree_to_list(root: Optional[TreeNode]) -> list:
    """Performs an in-order traversal to get a list of node values."""
    if not root:
        return []
    
    result = []
    # Standard in-order traversal: Left -> Root -> Right
    result.extend(tree_to_list(root.left))
    result.append(root.val)
    result.extend(tree_to_list(root.right))
    return result

class TestTrimBST(unittest.TestCase):
    
    def setUp(self):
        """Set up the Solution object before each test."""
        self.solution = Solution()

    # --- Test Case 1: Example 1 ---
    # Input: root = [1,0,2], low = 1, high = 2
    # Output: [1,null,2] (in-order: [1, 2])
    def test_example_one(self):
        # Build the input tree:
        #   1
        #  / \
        # 0   2
        root = TreeNode(1, TreeNode(0), TreeNode(2))
        low, high = 1, 2
        
        trimmed_root = self.solution.trimBST(root, low, high)
        expected_list = [1, 2]
        self.assertEqual(tree_to_list(trimmed_root), expected_list, 
                         "Test Case 1 failed: Example 1")

    # --- Test Case 2: Example 2 ---
    # Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    # Output: [3,2,null,1] (in-order: [1, 2, 3])
    def test_example_two(self):
        # Build the input tree:
        #       3
        #      / \
        #     0   4
        #      \ 
        #       2
        #      /
        #     1
        node1 = TreeNode(1)
        node2 = TreeNode(2, node1)
        node0 = TreeNode(0, None, node2)
        node4 = TreeNode(4)
        root = TreeNode(3, node0, node4)
        
        low, high = 1, 3
        
        trimmed_root = self.solution.trimBST(root, low, high)
        # Expected tree structure after trimming:
        #       3
        #      /
        #     2
        #    /
        #   1
        expected_list = [1, 2, 3] 
        self.assertEqual(tree_to_list(trimmed_root), expected_list, 
                         "Test Case 2 failed: Example 2")
        # Additionally, check the structure
        self.assertIsNotNone(trimmed_root)
        self.assertEqual(trimmed_root.val, 3)
        self.assertIsNotNone(trimmed_root.left)
        self.assertEqual(trimmed_root.left.val, 2)
        self.assertIsNone(trimmed_root.right)
        self.assertIsNotNone(trimmed_root.left.left)
        self.assertEqual(trimmed_root.left.left.val, 1)


    # --- Test Case 3: Trimming everything (returns None) ---
    def test_trim_all(self):
        # Input: root = [5, 2, 8], low = 10, high = 15
        root = TreeNode(5, TreeNode(2), TreeNode(8))
        low, high = 10, 15
        
        trimmed_root = self.solution.trimBST(root, low, high)
        self.assertIsNone(trimmed_root, 
                          "Test Case 3 failed: Should return None")

    # --- Test Case 4: Keeping only the root ---
    def test_keep_only_root(self):
        # Input: root = [10, 5, 15], low = 9, high = 11
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        low, high = 9, 11
        
        trimmed_root = self.solution.trimBST(root, low, high)
        expected_list = [10]
        self.assertEqual(tree_to_list(trimmed_root), expected_list, 
                         "Test Case 4 failed: Should keep only root")
        self.assertIsNone(trimmed_root.left)
        self.assertIsNone(trimmed_root.right)

    # --- Test Case 5: Root is out of bounds (small) and needs replacement ---
    # Input: root = [4, 2, 6], low = 5, high = 7
    # The new root should be 6.
    def test_new_root_from_right(self):
        root = TreeNode(4, TreeNode(2), TreeNode(6))
        low, high = 5, 7
        
        trimmed_root = self.solution.trimBST(root, low, high)
        expected_list = [6] 
        self.assertEqual(tree_to_list(trimmed_root), expected_list, 
                         "Test Case 5 failed: New root should be 6")
        self.assertIsNotNone(trimmed_root)
        self.assertEqual(trimmed_root.val, 6)
        self.assertIsNone(trimmed_root.left)
        self.assertIsNone(trimmed_root.right)


if __name__ == '__main__':
    # Run all the tests defined in TestTrimBST
    unittest.main(argv=['first-arg-is-ignored'], exit=False)