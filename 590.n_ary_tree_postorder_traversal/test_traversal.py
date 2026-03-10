import unittest
from typing import Optional, List
from traversal import Solution, Node


# --- Test Helper Function ---

def build_tree(data: List[Optional[int]]) -> Optional[Node]:
    """
    Constructs an N-ary tree from level-order serialization where None separates child groups.
    [1, None, 3, 2, 4, None, 5, 6] -> N-ary tree
    """
    if not data:
        return None

    root = Node(data[0], [])
    queue = [root]
    i = 2  # skip root and first null

    for node in queue:
        while i < len(data) and data[i] is not None:
            child = Node(data[i], [])
            node.children.append(child)
            queue.append(child)
            i += 1
        i += 1  # skip the null separator

    return root


# --- Unit Test Class ---

class TestPostorder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_example_1(self):
        """Test example 1: [1,null,3,2,4,null,5,6] -> [5,6,3,2,4,1]"""
        root = build_tree([1, None, 3, 2, 4, None, 5, 6])
        self.assertEqual(self.solution.postorder(root), [5, 6, 3, 2, 4, 1])

    def test_example_2(self):
        """Test example 2: deep tree -> [2,6,14,11,7,3,12,8,4,13,9,10,5,1]"""
        root = build_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
        self.assertEqual(self.solution.postorder(root), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])

    def test_empty_tree(self):
        """Test empty tree returns empty list."""
        self.assertEqual(self.solution.postorder(None), [])

    def test_single_node(self):
        """Test single node tree returns [val]."""
        root = Node(1, [])
        self.assertEqual(self.solution.postorder(root), [1])

    def test_two_levels(self):
        """Test root with two children: root=1, children=[2,3] -> [2,3,1]"""
        root = Node(1, [Node(2, []), Node(3, [])])
        self.assertEqual(self.solution.postorder(root), [2, 3, 1])

    def test_linear_chain(self):
        """Test chain: 1 -> 2 -> 3 -> postorder [3,2,1]"""
        root = Node(1, [Node(2, [Node(3, [])])])
        self.assertEqual(self.solution.postorder(root), [3, 2, 1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
