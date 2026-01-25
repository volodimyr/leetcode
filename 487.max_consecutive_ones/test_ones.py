import unittest
from ones import Solution


class TestFindMaxConsecutiveOnes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 0, 1, 1, 0]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 4)

    def test_example_2(self):
        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 4)

    def test_all_ones(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 4)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 1)

    def test_single_one(self):
        nums = [1]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 1)

    def test_single_zero(self):
        nums = [0]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 1)

    def test_zero_at_start(self):
        nums = [0, 1, 1, 1]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 4)

    def test_zero_at_end(self):
        nums = [1, 1, 1, 0]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 4)

    def test_multiple_zeros_spread(self):
        nums = [1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 5)

    def test_long_sequence(self):
        nums = [1] * 100000
        self.assertEqual(self.sol.findMaxConsecutiveOnes(nums), 100000)


if __name__ == "__main__":
    unittest.main()
