from typing import Optional, List
import unittest

from longest import Solution, TreeNode


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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


class TestLongestConsecutive(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # [1,null,3,2,4,null,null,null,5] -> 3-4-5
        root = build_tree([1, None, 3, 2, 4, None, None, None, 5])
        self.assertEqual(self.sol.longestConsecutive(root), 3)

    def test_example2(self):
        # [2,null,3,2,null,1] -> 2-3 (not 3-2-1)
        root = build_tree([2, None, 3, 2, None, 1])
        self.assertEqual(self.sol.longestConsecutive(root), 2)

    def test_single_node(self):
        root = build_tree([1])
        self.assertEqual(self.sol.longestConsecutive(root), 1)

    def test_all_consecutive_left_skewed(self):
        # 1-2-3-4 along left spine
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.sol.longestConsecutive(root), 4)

    def test_no_consecutive_path(self):
        # 5-3-1: decreasing, no consecutive path longer than 1
        root = build_tree([5, 3, 1])
        self.assertEqual(self.sol.longestConsecutive(root), 1)

    def test_consecutive_in_right_subtree(self):
        root = TreeNode(10)
        root.right = TreeNode(11)
        root.right.right = TreeNode(12)
        root.right.right.right = TreeNode(13)
        self.assertEqual(self.sol.longestConsecutive(root), 4)

    def test_consecutive_starts_mid_tree(self):
        # Root is 5, but 7-8-9 is the longest path starting at 7
        root = TreeNode(5)
        root.left = TreeNode(7)
        root.left.right = TreeNode(8)
        root.left.right.right = TreeNode(9)
        self.assertEqual(self.sol.longestConsecutive(root), 3)

    def test_two_nodes_consecutive(self):
        root = build_tree([3, 4])
        self.assertEqual(self.sol.longestConsecutive(root), 2)

    def test_two_nodes_not_consecutive(self):
        root = build_tree([3, 5])
        self.assertEqual(self.sol.longestConsecutive(root), 1)

    def test_negative_values_consecutive(self):
        root = TreeNode(-2)
        root.right = TreeNode(-1)
        root.right.right = TreeNode(0)
        self.assertEqual(self.sol.longestConsecutive(root), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
