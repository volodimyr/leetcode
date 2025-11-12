import unittest
from collections import deque
from reverse import Solution
from reverse import TreeNode

# --- helper functions ---
def build_tree(values):
    """Builds a binary tree (perfect) from a list using BFS."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(values)):
        if nodes[i] is not None:
            left_i, right_i = 2*i + 1, 2*i + 2
            if left_i < len(nodes):
                nodes[i].left = nodes[left_i]
            if right_i < len(nodes):
                nodes[i].right = nodes[right_i]
    return nodes[0]

def tree_to_list(root):
    """Convert binary tree back to list (level order)."""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left or node.right:
            q.append(node.left)
            q.append(node.right)
    return result


# --- test suite ---
class TestReverseOddLevels(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([2, 3, 5, 8, 13, 21, 34])
        expected = [2, 5, 3, 8, 13, 21, 34]
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)

    def test_example_2(self):
        root = build_tree([7, 13, 11])
        expected = [7, 11, 13]
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)

    def test_example_3(self):
        root = build_tree([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
        expected = [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)

    def test_single_node(self):
        root = build_tree([10])
        expected = [10]
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)

    def test_two_levels(self):
        root = build_tree([1,2,3])
        expected = [1,3,2]
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)

    def test_three_levels(self):
        root = build_tree([1,2,3,4,5,6,7])
        expected = [1,3,2,4,5,6,7]  # only level 1 reversed
        sol = Solution().reverseOddLevels(root)
        self.assertEqual(tree_to_list(sol), expected)


if __name__ == "__main__":
    unittest.main()
