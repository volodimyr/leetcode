import unittest
from prob import Solution

class TestMaxProbability(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def assertFloatAlmostEqual(self, a, b, eps=1e-5):
        self.assertTrue(abs(a - b) <= eps, f"{a} != {b}")

    def test_example_1(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.2]
        start, end = 0, 2
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.25)

    def test_example_2(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.3]
        start, end = 0, 2
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.3)

    def test_example_3_no_path(self):
        n = 3
        edges = [[0,1]]
        succProb = [0.5]
        start, end = 0, 2
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, 0.0)

    def test_direct_vs_indirect(self):
        n = 4
        edges = [[0,1],[1,2],[2,3],[0,3]]
        succProb = [0.9,0.9,0.9,0.5]
        start, end = 0, 3
        # indirect path: 0.9 * 0.9 * 0.9 = 0.729 > 0.5
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.729)

    def test_zero_probability_edges(self):
        n = 3
        edges = [[0,1],[1,2]]
        succProb = [0.0,1.0]
        start, end = 0, 2
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, 0.0)

    def test_single_path(self):
        n = 2
        edges = [[0,1]]
        succProb = [0.75]
        start, end = 0, 1
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.75)

    def test_cycle_graph(self):
        n = 4
        edges = [[0,1],[1,2],[2,0],[2,3]]
        succProb = [0.5,0.5,0.9,0.8]
        start, end = 0, 3
        # best: 0 -> 2 -> 3 = 0.9 * 0.8 = 0.72
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.72)

    def test_large_probabilities(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[3,4]]
        succProb = [0.99,0.99,0.99,0.99]
        start, end = 0, 4
        result = self.sol.maxProbability(n, edges, succProb, start, end)
        self.assertFloatAlmostEqual(result, 0.99**4)

if __name__ == "__main__":
    unittest.main()
