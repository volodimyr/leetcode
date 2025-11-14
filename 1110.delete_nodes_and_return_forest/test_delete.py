import unittest
from typing import Optional, List
from delete import TreeNode, Solution

class TestDeleteNodes(unittest.TestCase):
    
    def tree_to_list(self, root: Optional[TreeNode]) -> List:
        """Helper: Convert tree to level-order list for comparison"""
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
        # Remove trailing Nones
        while result and result[-1] is None:
            result.pop()
        return result
    
    def test_example_1(self):
        """Test case from example 1: delete nodes 3 and 5"""
        # Tree: [1,2,3,4,5,6,7]
        root = TreeNode(1,
                       TreeNode(2, TreeNode(4), TreeNode(5)),
                       TreeNode(3, TreeNode(6), TreeNode(7)))
        
        solution = Solution()
        result = solution.delNodes(root, [3, 5])
        
        # Convert results to lists for easier comparison
        result_lists = sorted([self.tree_to_list(tree) for tree in result])
        
        # Expected: [[1,2,null,4], [6], [7]]
        expected = sorted([[1, 2, None, 4], [6], [7]])
        
        self.assertEqual(result_lists, expected)
    
    def test_example_2(self):
        """Test case from example 2: delete node 3"""
        # Tree: [1,2,4,null,3]
        root = TreeNode(1,
                       TreeNode(2, None, TreeNode(3)),
                       TreeNode(4))
        
        solution = Solution()
        result = solution.delNodes(root, [3])
        
        result_lists = [self.tree_to_list(tree) for tree in result]
        expected = [[1, 2, 4]]
        
        self.assertEqual(result_lists, expected)
    
    def test_delete_root_only(self):
        """Delete only the root node"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        
        solution = Solution()
        result = solution.delNodes(root, [1])
        
        result_lists = sorted([self.tree_to_list(tree) for tree in result])
        expected = sorted([[2], [3]])
        
        self.assertEqual(result_lists, expected)
    
    def test_delete_nothing(self):
        """Delete no nodes - return original tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        
        solution = Solution()
        result = solution.delNodes(root, [])
        
        self.assertEqual(len(result), 1)
        self.assertEqual(self.tree_to_list(result[0]), [1, 2, 3])
    
    def test_delete_all_nodes(self):
        """Delete all nodes in tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        
        solution = Solution()
        result = solution.delNodes(root, [1, 2, 3])
        
        self.assertEqual(result, [])
    
    def test_single_node_delete(self):
        """Single node tree, delete it"""
        root = TreeNode(1)
        
        solution = Solution()
        result = solution.delNodes(root, [1])
        
        self.assertEqual(result, [])
    
    def test_single_node_keep(self):
        """Single node tree, keep it"""
        root = TreeNode(1)
        
        solution = Solution()
        result = solution.delNodes(root, [])
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].val, 1)
    
    def test_delete_leaf_nodes(self):
        """Delete only leaf nodes"""
        root = TreeNode(1,
                       TreeNode(2, TreeNode(4), TreeNode(5)),
                       TreeNode(3))
        
        solution = Solution()
        result = solution.delNodes(root, [4, 5, 3])
        
        self.assertEqual(len(result), 1)
        self.assertEqual(self.tree_to_list(result[0]), [1, 2])
    
    def test_delete_internal_nodes(self):
        """Delete internal nodes creating multiple forests"""
        root = TreeNode(1,
                       TreeNode(2, TreeNode(4), TreeNode(5)),
                       TreeNode(3, TreeNode(6), TreeNode(7)))
        
        solution = Solution()
        result = solution.delNodes(root, [2, 3])
        
        result_lists = sorted([self.tree_to_list(tree) for tree in result])
        expected = sorted([[1], [4], [5], [6], [7]])
        
        self.assertEqual(result_lists, expected)
    
    def test_linear_tree_delete_middle(self):
        """Linear tree (like linked list), delete middle node"""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        
        solution = Solution()
        result = solution.delNodes(root, [2])
        
        result_lists = sorted([self.tree_to_list(tree) for tree in result])
        expected = sorted([[1], [3, 4]])
        
        self.assertEqual(result_lists, expected)
    
    def test_delete_node_with_one_child(self):
        """Delete node that has only one child"""
        root = TreeNode(1,
                       TreeNode(2, TreeNode(4)),
                       TreeNode(3))
        
        solution = Solution()
        result = solution.delNodes(root, [2])
        
        result_lists = sorted([self.tree_to_list(tree) for tree in result])
        expected = sorted([[1, None, 3], [4]])
        
        self.assertEqual(result_lists, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)