import unittest
from collections import deque
from typing import Optional
from pointers import Solution, Node

# --- 3. Helper Functions for Test Setup and Verification ---

def build_perfect_tree(level_order_list: list[int]) -> Optional[Node]:
    """Builds a perfect binary tree from a level order list (assuming no 'None' values)."""
    if not level_order_list:
        return None
    
    nodes = [Node(val) for val in level_order_list]
    root = nodes[0]
    
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        parent = queue.popleft()
        
        # Left child
        if i < len(nodes):
            parent.left = nodes[i]
            queue.append(nodes[i])
            i += 1
            
        # Right child
        if i < len(nodes):
            parent.right = nodes[i]
            queue.append(nodes[i])
            i += 1
            
    return root

def serialize_with_next_pointers(root: Optional[Node]) -> list[Optional[int | str]]:
    """
    Verifies the tree by returning a level-order list, including '#' to mark 
    the end of a level (as shown in the problem output format).
    """
    if not root:
        return []
        
    result = []
    level_start = root
    
    while level_start:
        current = level_start
        # Traverse the current level using 'next' pointers
        while current:
            result.append(current.val)
            current = current.next
            
        # Add '#' to mark the end of the level
        result.append('#')
        
        # Move to the start of the next level (guaranteed to be level_start.left)
        level_start = level_start.left
        
    return result # Remove the trailing '#'

# --- 4. The Unit Test Class ---

class TestConnect(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the main example case: [1,2,3,4,5,6,7]"""
        # Input (built as a standard tree first)
        input_list = [1, 2, 3, 4, 5, 6, 7]
        root = build_perfect_tree(input_list)
        
        # Expected Output serialized with next pointers
        expected_output = [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

        # Act
        connected_root = self.solution.connect(root)
        
        # Assert
        actual_output = serialize_with_next_pointers(connected_root)
        self.assertEqual(actual_output, expected_output)

    def test_example_2_empty_tree(self):
        """Test the empty tree case: []"""
        root = build_perfect_tree([])
        expected_output = []
        
        connected_root = self.solution.connect(root)
        actual_output = serialize_with_next_pointers(connected_root)
        self.assertEqual(actual_output, expected_output)

    def test_single_node(self):
        """Test a tree with only the root node: [1]"""
        input_list = [1]
        root = build_perfect_tree(input_list)
        
        # Expected: 1 -> NULL
        expected_output = [1, '#']
        
        connected_root = self.solution.connect(root)
        actual_output = serialize_with_next_pointers(connected_root)
        self.assertEqual(actual_output, expected_output)
        self.assertIsNone(connected_root.next)

    def test_two_levels(self):
        """Test a tree with two levels: [1,2,3]"""
        input_list = [1, 2, 3]
        root = build_perfect_tree(input_list)
        
        # Expected: 1 -> NULL, 2 -> 3 -> NULL
        expected_output = [1, '#', 2, 3, '#']
        
        connected_root = self.solution.connect(root)
        actual_output = serialize_with_next_pointers(connected_root)
        self.assertEqual(actual_output, expected_output)
        
        # Specific pointer checks
        self.assertIsNone(connected_root.next)
        self.assertEqual(connected_root.left.next, connected_root.right)
        self.assertIsNone(connected_root.right.next)
        
# --- 5. Run the Tests ---
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)