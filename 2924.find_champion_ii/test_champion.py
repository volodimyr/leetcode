import unittest
from champion import Solution


class TestFindChampion(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        self.assertEqual(self.sol.findChampion(1, []), 0)

    def test_simple_chain(self):
        # 0 -> 1 -> 2
        n = 3
        edges = [[0, 1], [1, 2]]
        self.assertEqual(self.sol.findChampion(n, edges), 0)

    def test_multiple_roots(self):
        # 0 -> 2, 1 -> 3, 1 -> 2
        n = 4
        edges = [[0, 2], [1, 3], [1, 2]]
        self.assertEqual(self.sol.findChampion(n, edges), -1)

    def test_no_edges(self):
        # everyone is a champion
        n = 5
        edges = []
        self.assertEqual(self.sol.findChampion(n, edges), -1)

    def test_star_graph(self):
        # 0 is stronger than everyone
        n = 4
        edges = [[0, 1], [0, 2], [0, 3]]
        self.assertEqual(self.sol.findChampion(n, edges), 0)

    def test_reverse_star(self):
        # everyone stronger than 0
        n = 4
        edges = [[1, 0], [2, 0], [3, 0]]
        self.assertEqual(self.sol.findChampion(n, edges), -1)

    def test_two_nodes(self):
        n = 2
        edges = [[1, 0]]
        self.assertEqual(self.sol.findChampion(n, edges), 1)

    def test_large_chain(self):
        n = 100
        edges = [[i, i + 1] for i in range(n - 1)]
        self.assertEqual(self.sol.findChampion(n, edges), 0)


if __name__ == "__main__":
    unittest.main()
