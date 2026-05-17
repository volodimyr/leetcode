import unittest
from sum import TreeNode, Solution


def build(values: list) -> TreeNode:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_i, right_i = 2 * i + 1, 2 * i + 2
        if left_i < len(nodes):
            node.left = nodes[left_i]
        if right_i < len(nodes):
            node.right = nodes[right_i]
    return nodes[0]


class TestTwoSumBSTs(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # root1 = [2,1,4], root2 = [1,0,3], target = 5 -> True (2+3)
        root1 = build([2, 1, 4])
        root2 = build([1, 0, 3])
        self.assertTrue(self.sol.twoSumBSTs(root1, root2, 5))

    def test_example2(self):
        # root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18 -> False
        root1 = build([0, -10, 10])
        root2 = build([5, 1, 7, 0, 2])
        self.assertFalse(self.sol.twoSumBSTs(root1, root2, 18))

    def test_single_nodes_match(self):
        root1 = build([3])
        root2 = build([7])
        self.assertTrue(self.sol.twoSumBSTs(root1, root2, 10))

    def test_single_nodes_no_match(self):
        root1 = build([3])
        root2 = build([7])
        self.assertFalse(self.sol.twoSumBSTs(root1, root2, 9))

    def test_negative_values(self):
        root1 = build([-5])
        root2 = build([5])
        self.assertTrue(self.sol.twoSumBSTs(root1, root2, 0))

    def test_target_requires_root_of_each(self):
        root1 = build([2, 1, 4])
        root2 = build([1, 0, 3])
        self.assertTrue(self.sol.twoSumBSTs(root1, root2, 3))  # 2+1


if __name__ == "__main__":
    unittest.main()
