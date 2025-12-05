import unittest

from connected import Solution

class TestCountComponents(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.countComponents(3, [[0,1], [0,2]]), 1)

    def test_example_2(self):
        self.assertEqual(self.s.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]), 2)

    def test_no_edges(self):
        self.assertEqual(self.s.countComponents(5, []), 5)

    def test_single_node(self):
        self.assertEqual(self.s.countComponents(1, []), 1)

    def test_disconnected_pairs(self):
        self.assertEqual(self.s.countComponents(4, [[0,1], [2,3]]), 2)

    def test_chain_graph(self):
        self.assertEqual(self.s.countComponents(5, [[0,1], [1,2], [2,3], [3,4]]), 1)

    def test_star_graph(self):
        self.assertEqual(self.s.countComponents(5, [[0,1], [0,2], [0,3], [0,4]]), 1)

    def test_duplicate_edges(self):
        self.assertEqual(self.s.countComponents(2, [[0,1], [1,0], [1,0]]), 1)

    def test_isolated_node_among_edges(self):
        self.assertEqual(self.s.countComponents(4, [[0,1], [1,2]]), 2)

    def test_large_sparse(self):
        edges = [[i, i+1] for i in range(0, 48, 2)]
        self.assertEqual(self.s.countComponents(50, edges), 50 - len(edges))

if __name__ == "__main__":
    unittest.main()
