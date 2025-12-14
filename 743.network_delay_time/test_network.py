import unittest
from network import Solution

class TestNetworkDelayTime(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)

    def test_example_2(self):
        times = [[1, 2, 1]]
        n = 2
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 1)

    def test_example_3_unreachable(self):
        times = [[1, 2, 1]]
        n = 2
        k = 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -1)

    def test_single_node(self):
        times = []
        n = 1
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 0)

    def test_disconnected_graph(self):
        times = [[1, 2, 1], [3, 4, 1]]
        n = 4
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), -1)

    def test_multiple_paths_choose_shortest(self):
        times = [
            [1, 2, 10],
            [1, 3, 1],
            [3, 2, 1]
        ]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)

    def test_zero_weight_edges(self):
        times = [
            [1, 2, 0],
            [2, 3, 0]
        ]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 0)

    def test_cycle_graph(self):
        times = [
            [1, 2, 1],
            [2, 3, 1],
            [3, 1, 1]
        ]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 2)

    def test_star_topology(self):
        times = [
            [1, 2, 1],
            [1, 3, 2],
            [1, 4, 3],
            [1, 5, 4]
        ]
        n = 5
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 4)

    def test_large_weights(self):
        times = [
            [1, 2, 100],
            [2, 3, 100],
            [1, 3, 300]
        ]
        n = 3
        k = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), 200)


if __name__ == "__main__":
    unittest.main()
