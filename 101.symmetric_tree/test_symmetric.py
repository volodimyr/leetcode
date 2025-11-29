import unittest
from typing import Optional, List
from symmetric import Solution, TreeNode

# --- Test Helper Function ---

def create_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Helper function to construct a binary tree from a list (level-order traversal).
    [1, 2, 2, 3, 4, 4, 3] -> Tree
    """
    if not nodes:
        return None
    
    root_val = nodes[0]
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        current = queue.pop(0)
        
        # Add left child
        if i < len(nodes):
            left_val = nodes[i]
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
            i += 1
            
        # Add right child
        if i < len(nodes):
            right_val = nodes[i]
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
            i += 1
            
    return root

# --- Unit Test Class ---

class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        """Set up the Solution class instance for each test."""
        self.solution = Solution()

    def test_example_1_symmetric(self):
        """Test the standard symmetric example: [1, 2, 2, 3, 4, 4, 3]"""
        nodes = [1, 2, 2, 3, 4, 4, 3]
        root = create_tree(nodes)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_example_2_asymmetric(self):
        """Test the standard asymmetric example: [1, 2, 2, null, 3, null, 3]"""
        nodes = [1, 2, 2, None, 3, None, 3]
        root = create_tree(nodes)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_single_node(self):
        """Test the simplest case: [1]"""
        nodes = [1]
        root = create_tree(nodes)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_empty_tree(self):
        """Test the edge case of an empty tree: []"""
        nodes = []
        root = create_tree(nodes)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_skewed_tree_asymmetric(self):
        """Test a skewed (non-symmetric) tree: [1, 2, null, 3, null, 4]"""
        nodes = [1, 2, None, 3, None, 4]
        root = create_tree(nodes)
        self.assertFalse(self.solution.isSymmetric(root))
        
    def test_deeply_symmetric(self):
        """Test a deep and complex symmetric tree."""
        nodes = [1, 2, 2, 3, None, None, 3, 4, 5, 5, 4]
        root = create_tree(nodes)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_mismatched_values(self):
        """Test where structure is symmetric but values mismatch: [1, 2, 2, 3, 4, 3, 3]"""
        nodes = [1, 2, 2, 3, 4, 3, 3] # Inner nodes 4 and 3 are unequal
        root = create_tree(nodes)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_mismatched_structure(self):
        """Test where one side has a node and the mirror side is null: [1, 2, 2, 3, null, 3, null]"""
        nodes = [1, 2, 2, 3, None, 3, None] # left.right is null, right.left is 3
        root = create_tree(nodes)
        self.assertFalse(self.solution.isSymmetric(root))

# To run the tests from a script:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)