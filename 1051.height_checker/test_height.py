import unittest
from height import Solution

class TestHeightChecker(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [1, 1, 4, 2, 1, 3]
        self.assertEqual(self.solution.heightChecker(heights), 3)

    def test_example_2(self):
        heights = [5, 1, 2, 3, 4]
        self.assertEqual(self.solution.heightChecker(heights), 5)

    def test_example_3(self):
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.heightChecker(heights), 0)

    def test_single_element(self):
        heights = [10]
        self.assertEqual(self.solution.heightChecker(heights), 0)

    def test_all_same(self):
        heights = [2, 2, 2, 2]
        self.assertEqual(self.solution.heightChecker(heights), 0)

    def test_reverse_sorted(self):
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.heightChecker(heights), 4)

    def test_random_case(self):
        heights = [3, 3, 2, 1, 4]
        # expected = [1,2,3,3,4] → mismatches at indices 0,1,2,3 → 4
        self.assertEqual(self.solution.heightChecker(heights), 4)

    def test_large_range(self):
        heights = [100, 1, 100, 1]
        # expected = [1,1,100,100] → mismatches at 0,2 → 2
        self.assertEqual(self.solution.heightChecker(heights), 2)


if __name__ == "__main__":
    unittest.main()