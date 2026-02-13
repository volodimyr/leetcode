import unittest
from find import Solution  # your Solution class in find.py

class TestFindCriticalAndPseudoCriticalEdges(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        n = 5
        edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
        expected_critical = [0,1]
        expected_pseudo = [2,3,4,5]
        result = self.sol.findCriticalAndPseudoCriticalEdges(n, edges)
        # Sort inner lists for comparison since order doesn't matter
        self.assertEqual(sorted(result[0]), sorted(expected_critical))
        self.assertEqual(sorted(result[1]), sorted(expected_pseudo))

    def test_example2(self):
        n = 4
        edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
        expected_critical = []
        expected_pseudo = [0,1,2,3]
        result = self.sol.findCriticalAndPseudoCriticalEdges(n, edges)
        self.assertEqual(sorted(result[0]), sorted(expected_critical))
        self.assertEqual(sorted(result[1]), sorted(expected_pseudo))

    def test_all_edges_critical(self):
        n = 3
        edges = [[0,1,1],[1,2,2]]
        expected_critical = [0,1]
        expected_pseudo = []
        result = self.sol.findCriticalAndPseudoCriticalEdges(n, edges)
        self.assertEqual(sorted(result[0]), sorted(expected_critical))
        self.assertEqual(sorted(result[1]), sorted(expected_pseudo))

    def test_single_edge_graph(self):
        n = 2
        edges = [[0,1,10]]
        expected_critical = [0]
        expected_pseudo = []
        result = self.sol.findCriticalAndPseudoCriticalEdges(n, edges)
        self.assertEqual(result[0], expected_critical)
        self.assertEqual(result[1], expected_pseudo)


if __name__ == "__main__":
    unittest.main()
