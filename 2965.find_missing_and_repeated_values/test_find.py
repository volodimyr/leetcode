import unittest
from find import Solution


class TestFindMissingAndRepeatedValues(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.findMissingAndRepeatedValues([[1, 3], [2, 2]]), [2, 4])

    def test_example_2(self):
        self.assertEqual(self.sol.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]), [9, 5])

    def test_repeated_is_first(self):
        # 1 is repeated, 4 is missing
        self.assertEqual(self.sol.findMissingAndRepeatedValues([[1, 1], [3, 2]]), [1, 4])

    def test_repeated_is_last(self):
        # 4 is repeated, 1 is missing
        self.assertEqual(self.sol.findMissingAndRepeatedValues([[4, 3], [2, 4]]), [4, 1])

    def test_2x2_repeated_middle(self):
        # 2 is repeated, 3 is missing
        self.assertEqual(self.sol.findMissingAndRepeatedValues([[1, 2], [2, 4]]), [2, 3])

    def test_4x4(self):
        grid = [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12],
            [13, 14, 15, 1],
        ]
        # 1 is repeated, 16 is missing
        self.assertEqual(self.sol.findMissingAndRepeatedValues(grid), [1, 16])


if __name__ == "__main__":
    unittest.main()
