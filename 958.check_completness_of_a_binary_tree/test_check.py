import unittest
from check import Solution, TreeNode


def build(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    for i, node in enumerate(nodes):
        if node:
            left, right = 2 * i + 1, 2 * i + 2
            if left < len(nodes):
                node.left = nodes[left]
            if right < len(nodes):
                node.right = nodes[right]
    return nodes[0]


class TestIsCompleteTree(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.isCompleteTree(build([1, 2, 3, 4, 5, 6])))

    def test_example2(self):
        self.assertFalse(self.s.isCompleteTree(build([1, 2, 3, 4, 5, None, 7])))

    def test_single_node(self):
        self.assertTrue(self.s.isCompleteTree(build([1])))

    def test_full_tree(self):
        self.assertTrue(self.s.isCompleteTree(build([1, 2, 3, 4, 5, 6, 7])))

    def test_missing_right_child(self):
        self.assertTrue(self.s.isCompleteTree(build([1, 2, 3, 4])))

    def test_gap_in_last_level(self):
        self.assertFalse(self.s.isCompleteTree(build([1, 2, 3, None, 4])))


if __name__ == "__main__":
    unittest.main()
