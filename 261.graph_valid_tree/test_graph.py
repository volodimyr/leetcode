import unittest
from graph import Solution

class TestGraphValidTree(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_valid_tree(self):
        n = 5
        edges = [[0,1],[0,2],[0,3],[1,4]]
        self.assertTrue(self.sol.validTree(n, edges))

    def test_example_2_cycle(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        self.assertFalse(self.sol.validTree(n, edges))

    def test_single_node(self):
        n = 1
        edges = []
        self.assertTrue(self.sol.validTree(n, edges))

    def test_disconnected_graph(self):
        n = 4
        edges = [[0,1],[2,3]]
        self.assertFalse(self.sol.validTree(n, edges))

    def test_not_enough_edges(self):
        n = 4
        edges = [[0,1],[1,2]]
        self.assertFalse(self.sol.validTree(n, edges))

    def test_too_many_edges(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        self.assertFalse(self.sol.validTree(n, edges))

    def test_line_tree(self):
        n = 4
        edges = [[0,1],[1,2],[2,3]]
        self.assertTrue(self.sol.validTree(n, edges))

    def test_star_tree(self):
        n = 5
        edges = [[0,1],[0,2],[0,3],[0,4]]
        self.assertTrue(self.sol.validTree(n, edges))

    def test_cycle_with_correct_edge_count(self):
        n = 4
        edges = [[0,1],[1,2],[2,0]]
        self.assertFalse(self.sol.validTree(n, edges))


if __name__ == "__main__":
    unittest.main()
