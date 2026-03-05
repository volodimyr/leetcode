import unittest
from distance import Solution


class TestMaxDistance(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
        self.assertEqual(self.solution.maxDistance(arrays), 4)

    def test_example_2(self):
        arrays = [[1], [1]]
        self.assertEqual(self.solution.maxDistance(arrays), 0)

    def test_two_arrays(self):
        arrays = [[1, 4], [0, 5]]
        self.assertEqual(self.solution.maxDistance(arrays), 4)

    def test_negative_numbers(self):
        arrays = [[-10, -5], [-3, 0], [2, 4]]
        self.assertEqual(self.solution.maxDistance(arrays), 14)

    def test_single_element_arrays(self):
        arrays = [[1], [5], [10]]
        self.assertEqual(self.solution.maxDistance(arrays), 9)

    def test_large_gap(self):
        arrays = [[1, 2, 3], [10, 11], [20, 30]]
        self.assertEqual(self.solution.maxDistance(arrays), 29)

    def test_optimal_not_first_array(self):
        arrays = [[5, 6], [1, 2], [3, 4]]
        self.assertEqual(self.solution.maxDistance(arrays), 5)

    def test_all_negative(self):
        arrays = [[-20, -10], [-5, -1], [-30, -25]]
        self.assertEqual(self.solution.maxDistance(arrays), 29)


if __name__ == "__main__":
    unittest.main()