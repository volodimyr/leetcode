import unittest
from intersection import Solution


class TestIntervalIntersection(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        first = [[0,2],[5,10],[13,23],[24,25]]
        second = [[1,5],[8,12],[15,24],[25,26]]
        expected = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_example_2(self):
        first = [[1,3],[5,9]]
        second = []
        expected = []

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_empty_first_list(self):
        first = []
        second = [[1,5]]
        expected = []

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_no_overlap(self):
        first = [[1,2],[5,6]]
        second = [[3,4],[7,8]]
        expected = []

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_full_overlap(self):
        first = [[1,10]]
        second = [[2,3],[4,5],[6,7]]
        expected = [[2,3],[4,5],[6,7]]

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_touching_boundaries(self):
        first = [[1,5]]
        second = [[5,10]]
        expected = [[5,5]]

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)

    def test_single_point_intervals(self):
        first = [[5,5]]
        second = [[5,5]]
        expected = [[5,5]]

        result = self.solution.intervalIntersection(first, second)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()