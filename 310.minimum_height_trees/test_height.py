import unittest
from height import Solution


class TestMinimumHeightTrees(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        n = 1
        edges = []
        self.assertEqual(self.sol.findMinHeightTrees(n, edges), [0])

    def test_two_nodes(self):
        n = 2
        edges = [[0, 1]]
        result = self.sol.findMinHeightTrees(n, edges)
        self.assertCountEqual(result, [0, 1])

    def test_example_1(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        self.assertEqual(self.sol.findMinHeightTrees(n, edges), [1])

    def test_example_2(self):
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        result = self.sol.findMinHeightTrees(n, edges)
        self.assertCountEqual(result, [3, 4])

    def test_line_tree_odd(self):
        # 0 - 1 - 2 - 3 - 4
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.sol.findMinHeightTrees(n, edges), [2])

    def test_line_tree_even(self):
        # 0 - 1 - 2 - 3
        n = 4
        edges = [[0, 1], [1, 2], [2, 3]]
        result = self.sol.findMinHeightTrees(n, edges)
        self.assertCountEqual(result, [1, 2])

    def test_star_tree(self):
        #    1
        #    |
        # 4--0--2
        #    |
        #    3
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        self.assertEqual(self.sol.findMinHeightTrees(n, edges), [0])


if __name__ == "__main__":
    unittest.main()
