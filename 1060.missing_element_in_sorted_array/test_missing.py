import unittest
from missing import Solution

class TestMissingElement(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.missingElement([4, 7, 9, 10], 1), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.missingElement([4, 7, 9, 10], 3), 8)

    def test_example_3(self):
        self.assertEqual(self.solution.missingElement([1, 2, 4], 3), 6)

    def test_missing_beyond_array(self):
        self.assertEqual(self.solution.missingElement([4, 7, 9, 10], 4), 11)

    def test_single_element(self):
        self.assertEqual(self.solution.missingElement([5], 3), 8)

    def test_consecutive_with_gap_at_end(self):
        self.assertEqual(self.solution.missingElement([1, 2, 3], 2), 5)

    def test_large_k(self):
        self.assertEqual(self.solution.missingElement([1, 3], 5), 7)


if __name__ == "__main__":
    unittest.main()
