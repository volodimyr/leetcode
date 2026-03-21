import unittest
from distance import TreeNode, Solution


def build_tree(values: list) -> TreeNode:
    """Build a BST from a level-order list (None for missing nodes)."""
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


class TestMinDiffInBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # [4,2,6,1,3] -> min diff = 1
        root = build_tree([4, 2, 6, 1, 3])
        self.assertEqual(self.solution.minDiffInBST(root), 1)

    def test_example2(self):
        # [1,0,48,null,null,12,49] -> min diff = 1
        root = build_tree([1, 0, 48, None, None, 12, 49])
        self.assertEqual(self.solution.minDiffInBST(root), 1)

    def test_two_nodes(self):
        # Minimum valid tree
        root = build_tree([5, 3])
        self.assertEqual(self.solution.minDiffInBST(root), 2)

    def test_two_nodes_right(self):
        root = build_tree([3, None, 7])
        self.assertEqual(self.solution.minDiffInBST(root), 4)

    def test_consecutive_values(self):
        # All consecutive: 1,2,3,4,5 -> min diff = 1
        root = build_tree([3, 2, 4, 1, None, None, 5])
        self.assertEqual(self.solution.minDiffInBST(root), 1)

    def test_large_gap(self):
        # [1, null, 100000] -> min diff = 99999
        root = build_tree([1, None, 100000])
        self.assertEqual(self.solution.minDiffInBST(root), 99999)

    def test_single_level(self):
        # [10, 5, 15] -> min diff = 5
        root = build_tree([10, 5, 15])
        self.assertEqual(self.solution.minDiffInBST(root), 5)

    def test_skewed_left(self):
        # Left-skewed: 4->3->2->1, in-order [1,2,3,4] -> diff = 1
        root = TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))
        self.assertEqual(self.solution.minDiffInBST(root), 1)

    def test_skewed_right(self):
        # Right-skewed: 1->3->6->10, in-order [1,3,6,10] -> min diff = 2
        root = TreeNode(1, None, TreeNode(3, None, TreeNode(6, None, TreeNode(10))))
        self.assertEqual(self.solution.minDiffInBST(root), 2)


if __name__ == "__main__":
    unittest.main()
