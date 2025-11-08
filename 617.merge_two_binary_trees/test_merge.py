from typing import Optional, List
import unittest

from merge import Solution
from merge import TreeNode

class TestMergeTrees(unittest.TestCase):
    
    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper to build tree from level-order list"""
        if not values or values[0] is None:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Helper to convert tree to level-order list"""
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result
    
    def test_example1(self):
        """Test Example 1: [1,3,2,5] + [2,1,3,null,4,null,7] = [3,4,5,5,4,null,7]"""
        sol = Solution()
        root1 = self.build_tree([1, 3, 2, 5])
        root2 = self.build_tree([2, 1, 3, None, 4, None, 7])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [3, 4, 5, 5, 4, None, 7])
    
    def test_example2(self):
        """Test Example 2: [1] + [1,2] = [2,2]"""
        sol = Solution()
        root1 = self.build_tree([1])
        root2 = self.build_tree([1, 2])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [2, 2])
    
    def test_both_empty(self):
        """Test when both trees are empty"""
        sol = Solution()
        result = sol.mergeTrees(None, None)
        self.assertIsNone(result)
    
    def test_first_empty(self):
        """Test when first tree is empty"""
        sol = Solution()
        root2 = self.build_tree([1, 2, 3])
        result = sol.mergeTrees(None, root2)
        self.assertEqual(self.tree_to_list(result), [1, 2, 3])
    
    def test_second_empty(self):
        """Test when second tree is empty"""
        sol = Solution()
        root1 = self.build_tree([1, 2, 3])
        result = sol.mergeTrees(root1, None)
        self.assertEqual(self.tree_to_list(result), [1, 2, 3])
    
    def test_single_node_both(self):
        """Test with single nodes in both trees"""
        sol = Solution()
        root1 = self.build_tree([5])
        root2 = self.build_tree([3])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [8])
    
    def test_different_structures(self):
        """Test trees with different structures"""
        sol = Solution()
        root1 = self.build_tree([1, 2, None, 3])
        root2 = self.build_tree([1, None, 2, None, 3])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [2, 2, 2, 3, None, None, 3])
    
    def test_negative_values(self):
        """Test with negative values"""
        sol = Solution()
        root1 = self.build_tree([5, -3, 2])
        root2 = self.build_tree([-5, 3, -2])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [0, 0, 0])
    
    def test_one_sided_trees(self):
        """Test with one-sided trees"""
        sol = Solution()
        root1 = self.build_tree([1, 2, None, 3, None, 4])
        root2 = self.build_tree([1, None, 2, None, 3, None, 4])
        result = sol.mergeTrees(root1, root2)
        expected = [2, 2, 2, 3, None, None, 3, 4, None, None, 4]
        self.assertEqual(self.tree_to_list(result), expected)
    
    def test_larger_tree(self):
        """Test with larger trees"""
        sol = Solution()
        root1 = self.build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = self.build_tree([1, 2, 3, 4, 5, 6, 7])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [2, 4, 6, 8, 10, 12, 14])
    
    def test_zero_values(self):
        """Test with zero values"""
        sol = Solution()
        root1 = self.build_tree([0, 0, 0])
        root2 = self.build_tree([0, 0, 0])
        result = sol.mergeTrees(root1, root2)
        self.assertEqual(self.tree_to_list(result), [0, 0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)